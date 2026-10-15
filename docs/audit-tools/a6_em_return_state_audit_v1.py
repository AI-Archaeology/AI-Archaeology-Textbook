#!/usr/bin/env python3
"""A6 PR22: original compat-v3 EM convergence and return-state diagnostic.

Only 8 synthetic objects. Imports private compat-v3 created and validated by
PR21; temporarily wraps its e_step and m_step in memory to OBSERVE calls.
Does NOT patch any file, change the EM stopping rule, read the ivory corpus,
or run historical K sweeps. Outputs aggregated private reports only.
"""
from __future__ import annotations

import copy
import csv
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import traceback

ROOT = Path("downloads/private-workflow/a6-reproduction")
SOURCE = ROOT / "compat-v3/src/aneic/mfm.py"
REPORT = Path("downloads/private-review/a6-ivories")
CORE_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
checks = []
observations = []

def check(name, condition, detail):
    status = "PASS" if bool(condition) else "FAIL"
    checks.append((name, status, str(detail)))
    print(f"{status} | {name} | {detail}")

def observe(name, result):
    observations.append((name, str(result)))
    print(f"OBSERVED | {name} | {result}")

def git_head(root):
    result = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                            capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None

def save(stage, extra=None):
    REPORT.mkdir(parents=True, exist_ok=True)
    with (REPORT/"A6_EM_RETURN_STATE_CHECKS_PRIVATE.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(("check", "status", "detail"))
        w.writerows(checks)
    with (REPORT/"A6_EM_RETURN_STATE_OBSERVATIONS_PRIVATE.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(("observation", "value"))
        w.writerows(observations)
    passed = sum(s == "PASS" for _,s,_ in checks)
    failed = len(checks)-passed
    meta = {
        "stage": stage, "status": "PASS" if not failed else "FAIL",
        "passed": passed, "failed": failed,
        "limitations": [
            "PASS means trace and analytical checks succeeded, not convergence.",
            "Return-state offsets, if observed, are diagnostic findings, not errors in tracing.",
            "No historical stopping condition or prior formula is modified.",
            "Eight invented observations only; real corpus not accessed.",
            "No author publication results reproduced."
        ]
    }
    if extra: meta.update(extra)
    (REPORT/"A6_EM_RETURN_STATE_REPORT_PRIVATE.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"\nOVERALL: {meta['status']} — {passed} PASS / {failed} FAIL")
    print("PRIVATE reports:", REPORT)
    return failed == 0

def same_params(left, right, np):
    return all(
        np.allclose(left[k].to_numpy(dtype=float),
                    right[k].to_numpy(dtype=float), rtol=1e-12, atol=1e-12)
        for k in ("pi", "mu", "l", "rho")
    )

def main():
    check("Historical core fixed Git commit",
          git_head(ROOT/"aneic-core") == CORE_SHA,git_head(ROOT/"aneic-core"))
    check("Previously verified private compat-v3 exists",SOURCE.is_file(),SOURCE)
    if any(x[1]=="FAIL" for x in checks):
        save("input validation")
        return 1
    import numpy as np
    import pandas as pd
    import scipy
    spec=importlib.util.spec_from_file_location("a6_aneic_em_state_observation_v1",SOURCE)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    script=SOURCE.read_text(encoding="utf-8")
    stop="if it > 1 and ((dL < eps) or it > max_iter):"
    check("Original stopping expression preserved in compat-v3",stop in script,stop)

    # Two isolated, purely synthetic cluster runs:
    # 8 objects, 1 numeric + 1 categorical feature, one value missing in each.
    idx=[f"toy-{i:02d}" for i in range(1,9)]
    real=pd.DataFrame({"x":[-2.,-1.1,-.3,.4,1.,1.6,2.5,float("nan")]},index=idx)
    cat=m.convert_indicator(pd.DataFrame(
        {"cat":["A","A","B","A","B","B","B",None]},index=idx))
    u={"a":2.0,
       "b":pd.DataFrame({0:[2.],1:[2.]},index=["x"]),
       "alpha":None,"beta":None}

    records=[]
    original_e=m.e_step
    original_m=m.m_step

    def wrapped_e(real_, cat_, pi, mu, precision, rho, *priors):
        params={"pi":pi.copy(deep=True),"mu":mu.copy(deep=True),
                "l":precision.copy(deep=True),"rho":rho.copy(deep=True)}
        gamma, objective=original_e(real_,cat_,pi,mu,precision,rho,*priors)
        records.append({"kind":"E", "params":params,
                        "gamma":gamma.copy(deep=True),"L":float(objective)})
        return gamma,objective

    def wrapped_m(real_,cat_,gamma,*priors):
        result=original_m(real_,cat_,gamma,*priors)
        records.append({"kind":"M", "params":{
            "pi":result[0].copy(deep=True),"mu":result[1].copy(deep=True),
            "l":result[2].copy(deep=True),"rho":result[3].copy(deep=True)}})
        return result

    m.e_step=wrapped_e
    m.m_step=wrapped_m
    try:
        np.random.seed(17)
        q,g,L,g0=m.em(real,cat,K=2,u=u,eps=1e-8,max_iter=3)
    finally:
        m.e_step=original_e
        m.m_step=original_m

    e=[r for r in records if r["kind"]=="E"]
    m_calls=[r for r in records if r["kind"]=="M"]
    check("At least two E evaluations recorded",len(e)>=2,len(e))
    check("Objective trace contains finite values",
          len(L)>0 and np.isfinite(np.asarray(L,dtype=float)).all(),len(L))
    if len(e)<2 or not L:
        save("insufficient trace")
        return 1

    check("Objective log records all but the final E evaluation",
          len(e)==len(L)+1 and
          np.allclose(np.asarray(L,dtype=float),
                      np.asarray([r["L"] for r in e[:-1]],dtype=float)),
          f"E calls={len(e)}, recorded objectives={len(L)}")
    check("Returned q equals parameters at preceding E evaluation",
          same_params(q,e[-2]["params"],np),
          "q is a prior accepted iteration snapshot")
    check("Returned gamma equals final E evaluation",
          np.allclose(g.to_numpy(dtype=float),
                      e[-1]["gamma"].to_numpy(dtype=float),atol=1e-12,rtol=1e-12),
          "gamma is computed at stopping iteration")
    check("Final E input parameters differ from returned q",
          not same_params(q,e[-1]["params"],np),
          "difference is a return-state phase offset, not automatically a bug")
    check("Recorded last objective corresponds to returned q",
          math.isclose(float(L[-1]),float(e[-2]["L"]),rel_tol=1e-12,abs_tol=1e-12),
          "last logged L matches preceding E-state")
    check("Final E objective absent from returned L",
          len(e)==len(L)+1,f"final objective={e[-1]['L']:.10f}")
    check("M update call count is consistent with original loop",
          len(m_calls)==len(e),f"E calls={len(e)}, M calls={len(m_calls)}")
    check("Responsibility normalization",
          bool(np.allclose(g.sum(axis=1).to_numpy(dtype=float),1)),
          "each synthetic object's responsibility sums to 1")
    check("Fixed Git commit still unchanged",
          git_head(ROOT/"aneic-core")==CORE_SHA,git_head(ROOT/"aneic-core"))

    # Separate PURE stop-condition truth table, no model execution.
    # In the author's condition, ANY negative relative delta is below eps.
    eps=1e-3
    negative_drop = (-0.02 < eps)
    exact_boundary = (4 > 3)
    check("A negative objective delta satisfies author's dL < eps test",
          negative_drop, "dL=-0.02 and eps=0.001; decline can trigger a stop")
    check("Strict > max_iter is true at max_iter+1, not max_iter",
          exact_boundary and not (3>3),
          "it=4 > 3; it=3 > 3 is false")
    observe("Historical stop predicate",stop)
    observe("Recorded objective sequence", [round(float(x),10) for x in L])
    observe("Final evaluated objective, not returned in L",round(float(e[-1]["L"]),10))
    observe("Final objective relative change",
            float((e[-1]["L"]-float(L[-1]))/abs(float(L[-1]))))
    observe("Returned q and gamma from identical evaluated state",
            same_params(q,e[-1]["params"],np))
    observe("Synthetic E/M trace call counts",{"E":len(e),"M":len(m_calls)})
    return 0 if save("original-control-flow trace on synthetic input",{
        "python":sys.version.split()[0],
        "numpy":np.__version__,"pandas":pd.__version__,"scipy":scipy.__version__,
        "seed":17,"K":2,"max_iter":3,
        "recorded_L":[float(x) for x in L],
        "last_unrecorded_e_objective":float(e[-1]["L"]),
        "returned_q_matches_final_e_state":same_params(q,e[-1]["params"],np)
    }) else 1

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as error:
        check("Unexpected runtime exception",False,type(error).__name__+": "+str(error))
        save("exception",{"traceback":traceback.format_exc(limit=8)})
        raise

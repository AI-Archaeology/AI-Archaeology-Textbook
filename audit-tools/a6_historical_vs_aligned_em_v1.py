#!/usr/bin/env python3
"""A6 PR23: compare historical vs state-aligned outputs of original ANEIC em().

Calls actual compat-v3 em() and a PRIVATE compat-v4 with ONE return-statement
change, on eight wholly invented examples. Stopping, priors, initialization,
e_step and m_step are identical in both programs. No original checkout edits,
no real ivory records and no historical full experimental replication.
"""
from __future__ import annotations

import csv
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import traceback

BASE = Path("downloads/private-workflow/a6-reproduction")
V3 = BASE / "compat-v3/src/aneic/mfm.py"
V4 = BASE / "compat-v4/src/aneic/mfm.py"
OUT = Path("downloads/private-review/a6-ivories")
CORE_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
ORIGINAL_RETURN = "    return q, g, L, g0"
ALIGNED_RETURN = "    return q_, g, L + [L_], g0"
STOP = "if it > 1 and ((dL < eps) or it > max_iter):"
checks = []
observations = []

def check(label, ok, detail):
    status = "PASS" if bool(ok) else "FAIL"
    checks.append((label, status, str(detail)))
    print(status, "|", label, "|", detail)

def observe(label, value):
    observations.append((label, str(value)))
    print("OBSERVED |", label, "|", value)

def commit(root):
    result = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                            text=True, capture_output=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None

def report(stage, metadata=None):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT/"A6_HISTORICAL_VS_ALIGNED_CHECKS_PRIVATE.csv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        w=csv.writer(f);w.writerow(("check","status","detail"));w.writerows(checks)
    with (OUT/"A6_HISTORICAL_VS_ALIGNED_OBSERVATIONS_PRIVATE.csv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        w=csv.writer(f);w.writerow(("observation","value"));w.writerows(observations)
    passed=sum(x[1]=="PASS" for x in checks)
    failed=len(checks)-passed
    data={
        "stage":stage,"passed":passed,"failed":failed,
        "status":"PASS" if failed==0 else "FAIL",
        "limits":[
            "Only toy data; not the original article's run.",
            "Compat-v4 changes only the return packaging; stopping is unchanged.",
            "Alignment does not establish convergence or MAP objective correctness.",
            "PASS includes successful detection of output differences.",
            "Original fixed repository remains untouched."
        ]}
    if metadata: data.update(metadata)
    (OUT/"A6_HISTORICAL_VS_ALIGNED_REPORT_PRIVATE.json").write_text(
        json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"\nOVERALL: {data['status']} — {passed} PASS / {failed} FAIL")
    print("PRIVATE reports:",OUT)
    return failed==0

def same_frame(a,b,np):
    return a.shape==b.shape and np.allclose(
        a.to_numpy(dtype=float),b.to_numpy(dtype=float),
        atol=1e-12,rtol=1e-12)

def same_model(a,b,np):
    return all(same_frame(a[k],b[k],np) for k in ("pi","mu","l","rho"))

def read_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def main():
    check("Historical fixed Git commit unchanged",
          commit(BASE/"aneic-core")==CORE_SHA,commit(BASE/"aneic-core"))
    check("Verified private compat-v3 exists",V3.is_file(),V3)
    if any(c[1]=="FAIL" for c in checks):
        report("preflight");return 1
    s=V3.read_text(encoding="utf-8")
    em_anchor="\ndef em(real, cat, K=None, u=None, eps=1e-5, max_iter=100, g0=None, theta0=None):"
    check("Single original em anchor",s.count(em_anchor)==1,s.count(em_anchor))
    prefix,em=s.split(em_anchor,1)
    check("Single original return statement in em",em.count(ORIGINAL_RETURN)==1,em.count(ORIGINAL_RETURN))
    check("Unmodified historical stop predicate present",em.count(STOP)==1,em.count(STOP))
    if any(c[1]=="FAIL" for c in checks):
        report("patch anchors");return 1
    repaired=prefix+em_anchor+em.replace(ORIGINAL_RETURN,ALIGNED_RETURN,1)
    V4.parent.mkdir(parents=True,exist_ok=True)
    if V4.exists():
        check("Existing private compat-v4 matches expected content",
              V4.read_text(encoding="utf-8")==repaired,"no overwrite")
    else:
        V4.write_text(repaired,encoding="utf-8")
        check("Private compat-v4 created",True,V4)
    if checks[-1][1]=="FAIL":
        report("private copy conflict");return 1
    diff="".join(difflib.unified_diff(
        s.splitlines(True),repaired.splitlines(True),
        fromfile="PRIVATE/compat-v3/mfm.py",tofile="PRIVATE/compat-v4/mfm.py"))
    (V4.parent.parent.parent/"A6_V3_TO_V4_PATCH_PRIVATE.patch").write_text(
        diff,encoding="utf-8")
    check("Return-only single-line change",bool(diff) and
          repaired.replace(ALIGNED_RETURN,ORIGINAL_RETURN,1)==s,
          "all other statements, including stopping, unchanged")

    import numpy as np
    import pandas as pd
    import scipy
    original=read_module("a6_original_control",V3)
    aligned=read_module("a6_aligned_return",V4)
    labels=["A","A","B","A","B","B","B",None]
    ix=[f"toy-{i:02d}" for i in range(1,9)]
    raw=pd.DataFrame({"cat":labels},index=ix)
    real=pd.DataFrame({"x":[-2.,-1.1,-.3,.4,1.,1.6,2.5,float("nan")]},index=ix)
    args={"K":2,"u":{"a":2.0,
         "b":pd.DataFrame({0:[2.0],1:[2.0]},index=["x"]),
         "alpha":None,"beta":None},"eps":1e-8,"max_iter":3}
    trajectories=[]
    for model in (original,aligned):
        np.random.seed(17)
        cat=model.convert_indicator(raw)
        records=[]
        real_e=model.e_step
        def spy_e(*a,**kw):
            gamma,score=real_e(*a,**kw)
            records.append({"pi":a[2].copy(deep=True),
                            "mu":a[3].copy(deep=True),
                            "l":a[4].copy(deep=True),
                            "rho":a[5].copy(deep=True),
                            "g":gamma.copy(deep=True),"score":float(score)})
            return gamma,score
        model.e_step=spy_e
        try:
            q,g,L,g0=model.em(real,cat,**args)
        finally:
            model.e_step=real_e
        trajectories.append((q,g,L,g0,records))
    (qh,gh,Lh,g0h,th),(qa,ga,La,g0a,ta)=trajectories
    check("Identical E-step counts",len(th)==len(ta) and len(th)>1,
          f"historic={len(th)}, aligned={len(ta)}")
    check("Identical computed E objectives",
          np.allclose([r["score"] for r in th],[r["score"] for r in ta],atol=1e-12),
          "same seeds and complete numerical sequence")
    check("Identical initial responsibilities",same_frame(g0h,g0a,np),
          "same seed=17")
    check("Same gamma returned by both policies",same_frame(gh,ga,np),
          "return packaging does not recalculate gamma")
    check("Historical log omits final E result",
          len(Lh)==len(th)-1 and
          np.allclose(Lh,[r["score"] for r in th[:-1]]),
          f"historical L={len(Lh)} vs E={len(th)}")
    check("Aligned log includes final E result",
          len(La)==len(ta) and
          np.allclose(La,[r["score"] for r in ta]),
          f"aligned L={len(La)} vs E={len(ta)}")
    check("Historical q matches penultimate E parameters",
          same_model(qh,th[-2],np),"historical accepted snapshot")
    check("Aligned q matches final E parameters",
          same_model(qa,ta[-1],np),"same state as aligned gamma")
    check("Historical q and final E parameter set differ",
          not same_model(qh,th[-1],np),
          "expected state discrepancy measured on synthetic input")
    check("Aligned gamma comes from aligned q",
          same_frame(ga,ta[-1]["g"],np) and same_model(qa,ta[-1],np),
          "q, gamma and latest score correspond")
    check("Aligned mixture proportions and posterior normalize",
          np.isclose(float(qa["pi"].sum()),1) and
          bool(np.allclose(ga.sum(axis=1).to_numpy(),1)),
          "mixture and row probabilities are normalized")
    check("Original stopping rule unchanged in both versions",
          STOP in s and STOP in repaired,"no convergence policy replacement")
    check("Original Git commit unchanged after both runs",
          commit(BASE/"aneic-core")==CORE_SHA,commit(BASE/"aneic-core"))

    final=float(La[-1]); previous=float(Lh[-1])
    delta=(final-previous)/abs(previous)
    observe("Historical objective trace",[round(float(x),10) for x in Lh])
    observe("Aligned objective trace",[round(float(x),10) for x in La])
    observe("Final objective omitted historically",round(final,10))
    observe("Difference in returned q",not same_model(qh,qa,np))
    observe("Relative last objective change",delta)
    observe("Maximum iteration setting",args["max_iter"])
    observe("Stop predicate at final step",{
        "dL_lt_eps":bool(delta<args["eps"]),
        "it_gt_max_iter":bool((len(ta)-1)>args["max_iter"])})
    return 0 if report("synthetic historical-versus-aligned return comparison",{
        "K":2,"seed":17,"max_iter":3,"eps":1e-8,
        "python":sys.version.split()[0],"numpy":np.__version__,
        "pandas":pd.__version__,"scipy":scipy.__version__,
        "historical_objective":[float(x) for x in Lh],
        "aligned_objective":[float(x) for x in La],
        "last_relative_change":float(delta),
        "compat_v3_sha256":hashlib.sha256(s.encode()).hexdigest(),
        "compat_v4_sha256":hashlib.sha256(repaired.encode()).hexdigest()
    }) else 1

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as exc:
        check("Unexpected runtime or model error",False,type(exc).__name__+": "+str(exc))
        report("runtime exception",{"traceback":traceback.format_exc(limit=8)})
        raise

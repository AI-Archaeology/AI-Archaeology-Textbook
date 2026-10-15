#!/usr/bin/env python3
"""A6 PR24: bounded stopping-policy comparison on invented observations ONLY.

Historical = previously tested private compat-v4 (aligned return state).
Candidate = compat-v5 with only ONE stopping-predicate change.
Other code, prior settings, synthetic observations, and seed remain identical.
Never edits original Git clones or reads official corpus; no historic result claims.
"""
from __future__ import annotations
import csv
import difflib
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import traceback

ROOT = Path("downloads/private-workflow/a6-reproduction")
OLD = ROOT/"compat-v4/src/aneic/mfm.py"
NEW = ROOT/"compat-v5/src/aneic/mfm.py"
OUT = Path("downloads/private-review/a6-ivories")
ORIGINAL_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
HIST = "if it > 1 and ((dL < eps) or it > max_iter):"
CAND = "if it > 1 and (((0 <= dL) and (dL < eps)) or it >= max_iter):"
checks = []
observations = []

def check(name, passed, detail):
    status = "PASS" if bool(passed) else "FAIL"
    checks.append((name,status,str(detail)))
    print(f"{status} | {name} | {detail}")

def observe(name, value):
    observations.append((name,json.dumps(value,ensure_ascii=False)))
    print(f"OBSERVED | {name} | {value}")

def git_head(path):
    p=subprocess.run(["git","-C",str(path),"rev-parse","HEAD"],
                     text=True,capture_output=True,check=False)
    return p.stdout.strip() if p.returncode==0 else None

def save(stage, payload=None):
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"A6_STOPPING_ROBUSTNESS_CHECKS_PRIVATE.csv").open("w",encoding="utf-8",newline="") as h:
        w=csv.writer(h);w.writerow(["check","status","detail"]);w.writerows(checks)
    with (OUT/"A6_STOPPING_ROBUSTNESS_OBSERVATIONS_PRIVATE.csv").open("w",encoding="utf-8",newline="") as h:
        w=csv.writer(h);w.writerow(["observation","value"]);w.writerows(observations)
    good=sum(s=="PASS" for _,s,_ in checks)
    bad=len(checks)-good
    data={"stage":stage,"passed":good,"failed":bad,"status":"PASS" if bad==0 else "FAIL",
          "caveats":[
              "Proposal is a controlled alternative stopping rule, not proof of canonical EM convergence.",
              "max_iter bounds loop condition, not necessarily exact E/M call count.",
              "Synthetic-only tests do not certify MAP objective or 2014 published partitions.",
              "No raw ivory records, historical restarts or K selection executed.",
              "A negative objective step is classified as diagnostic, not silently corrected."
          ]}
    if payload:data.update(payload)
    (OUT/"A6_STOPPING_ROBUSTNESS_REPORT_PRIVATE.json").write_text(
        json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"\nOVERALL: {data['status']} — {good} PASS / {bad} FAIL")
    print("PRIVATE reports:",OUT)
    return not bad

def import_file(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    check("Historical core remains fixed",
          git_head(ROOT/"aneic-core")==ORIGINAL_SHA,git_head(ROOT/"aneic-core"))
    check("Verified aligned private compat-v4 available",OLD.is_file(),OLD)
    if any(s=="FAIL" for _,s,_ in checks):
        save("preflight");return 1
    src=OLD.read_text(encoding="utf-8")
    check("Single historical stopping statement",src.count(HIST)==1,src.count(HIST))
    check("Aligned v4 return state is retained",
          src.count("    return q_, g, L + [L_], g0")==1,"one aligned return")
    if any(s=="FAIL" for _,s,_ in checks):
        save("anchors");return 1
    candidate=src.replace(HIST,CAND,1)
    NEW.parent.mkdir(parents=True,exist_ok=True)
    if NEW.exists():
        check("Preexisting private compat-v5 is identical",
              NEW.read_text(encoding="utf-8")==candidate,"never overwrite differences")
    else:
        NEW.write_text(candidate,encoding="utf-8")
        check("New private compat-v5 created",True,NEW)
    if checks[-1][1]=="FAIL":
        save("copy conflict");return 1
    diff="".join(difflib.unified_diff(src.splitlines(True),candidate.splitlines(True),
                     fromfile="PRIVATE/compat-v4/mfm.py",tofile="PRIVATE/compat-v5/mfm.py"))
    (ROOT/"compat-v5/A6_V4_TO_V5_PATCH_PRIVATE.patch").write_text(diff,encoding="utf-8")
    check("Only stopping statement differs",
          candidate.replace(CAND,HIST,1)==src and bool(diff),
          "one predicate modification; no other source changes")
    # Pure independently specified truth-table checks.
    eps=0.001
    hist=lambda it,d,maxit: it>1 and ((d<eps) or it>maxit)
    improved=lambda it,d,maxit: it>1 and (((0<=d) and (d<eps)) or it>=maxit)
    check("Negative objective delta distinguishes stopping rules",
          hist(2,-.02,5) and not improved(2,-.02,5),
          "it=2, dL=-0.02, eps=.001, cap=5")
    check("Positive small improvement stops in both",
          hist(2,.0002,5) and improved(2,.0002,5),
          "it=2, dL=.0002")
    check("Maximum-iteration boundary is explicit",
          not hist(5,.1,5) and improved(5,.1,5),
          "historical it>5 false at 5; candidate it>=5 true")
    check("Large positive improvement does not masquerade as convergence",
          not hist(2,.02,5) and not improved(2,.02,5),
          "it=2, dL=.02")
    import numpy as np
    import pandas as pd
    import scipy
    mods=[import_file("a6_stop_historical_v4",OLD),
          import_file("a6_stop_candidate_v5",NEW)]
    ids=[f"toy-{i:02d}" for i in range(1,9)]
    real=pd.DataFrame({"x":[-2.,-1.1,-.3,.4,1.,1.6,2.5,float("nan")]},index=ids)
    raw=pd.DataFrame({"cat":["A","A","B","A","B","B","B",None]},index=ids)
    setups=[(17,4,1e-8),(23,4,1e-8),(41,5,1e-6)]
    all_results=[]
    for seed,cap,tolerance in setups:
        traces=[]
        for module in mods:
            np.random.seed(seed)
            categories=module.convert_indicator(raw)
            u={"a":2.0,"b":pd.DataFrame({0:[2.],1:[2.]},index=["x"]),
               "alpha":None,"beta":None}
            evaluated=[]
            old_e=module.e_step
            def spy(*args,**kwargs):
                responsibility, objective=old_e(*args,**kwargs)
                evaluated.append(float(objective))
                return responsibility,objective
            module.e_step=spy
            try:
                q,g,L,g0=module.em(real,categories,K=2,u=u,eps=tolerance,max_iter=cap)
            finally:
                module.e_step=old_e
            traces.append({"q":q,"g":g,"L":[float(v) for v in L],
                           "computed":evaluated,"g0":g0})
        hist_result,cand_result=traces
        prefix=min(len(hist_result["computed"]),len(cand_result["computed"]))
        same_prefix=bool(np.allclose(hist_result["computed"][:prefix],
                                     cand_result["computed"][:prefix],
                                     atol=1e-11,rtol=1e-11))
        check(f"Seed {seed}: identical computed objective prefix",same_prefix,
              f"shared E evaluations={prefix}")
        check(f"Seed {seed}: finite objectives and normalized posterior",
              all(np.isfinite(t["computed"]).all() and
                  np.allclose(t["g"].sum(axis=1).to_numpy(),1.)
                  for t in traces),f"historical E={len(hist_result['computed'])}, candidate E={len(cand_result['computed'])}")
        check(f"Seed {seed}: final returned L matches last computed E",
              all(len(t["L"])==len(t["computed"]) and
                  np.isclose(t["L"][-1],t["computed"][-1]) for t in traces),
              "both policies use aligned output inherited from compat-v4")
        observe(f"Seed {seed}: policy comparison",{
            "max_iter":cap,"eps":tolerance,
            "historical_E":len(hist_result["computed"]),
            "candidate_E":len(cand_result["computed"]),
            "historical_last_L":hist_result["L"][-1],
            "candidate_last_L":cand_result["L"][-1],
            "same_prefix":same_prefix})
        all_results.append({"seed":seed,"max_iter":cap,"eps":tolerance,
                            "historical_e_calls":len(hist_result["computed"]),
                            "candidate_e_calls":len(cand_result["computed"]),
                            "same_prefix":same_prefix})
    check("Original author code still unchanged",git_head(ROOT/"aneic-core")==ORIGINAL_SHA,
          git_head(ROOT/"aneic-core"))
    return 0 if save("synthetic stopping robustness comparison",{
        "python":sys.version.split()[0],"numpy":np.__version__,
        "pandas":pd.__version__,"scipy":scipy.__version__,
        "historical_source_sha256":hashlib.sha256(src.encode()).hexdigest(),
        "candidate_sha256":hashlib.sha256(candidate.encode()).hexdigest(),
        "setups":all_results}) else 1

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as ex:
        check("Unexpected runtime failure",False,type(ex).__name__+": "+str(ex))
        save("exception",{"traceback":traceback.format_exc(limit=8)})
        raise

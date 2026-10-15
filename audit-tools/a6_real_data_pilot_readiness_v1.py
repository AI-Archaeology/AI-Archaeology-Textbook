#!/usr/bin/env python3
"""A6 PR25: read-only pilot readiness / reproducibility gate.

No original code is imported. No EM, fitting, results, plots, or object-wise
records are produced. All reports remain under ignored downloads/private-review.
This tool NEVER grants research approval based solely on technical PASS checks.
"""
from __future__ import annotations
import csv
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

BASE=Path("downloads/private-workflow/a6-reproduction")
INPUT=Path("downloads/official/levantine_corpus_gansell.csv")
OUT=Path("downloads/private-review/a6-ivories")
CORE_SHA="43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
SCRIPT_SHA="c45445a0e090853c6eb544bffe8042557e4db440"
DATA_SHA="d52ed8033ad7304024e207e02117d2cc1b425da8799e582858dac8a6b0b90941"
FILES={
 "compat-v1":BASE/"compat-v1/src/aneic/mfm.py",
 "compat-v2":BASE/"compat-v2/src/aneic/mfm.py",
 "compat-v3":BASE/"compat-v3/src/aneic/mfm.py",
 "compat-v4":BASE/"compat-v4/src/aneic/mfm.py",
 "compat-v5":BASE/"compat-v5/src/aneic/mfm.py",
}
checks=[]
holds=[]

def check(name, ok, detail):
    state="PASS" if ok else "FAIL"
    checks.append((name,state,str(detail)))
    print(f"{state} | {name} | {detail}")

def hold(name, reason):
    holds.append((name,str(reason)))
    print(f"HOLD | {name} | {reason}")

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def commit(path):
    r=subprocess.run(["git","-C",str(path),"rev-parse","HEAD"],
                     capture_output=True,text=True,check=False)
    return r.stdout.strip() if r.returncode==0 else None

def working_tree_clean(path):
    r=subprocess.run(["git","-C",str(path),"status","--porcelain"],
                     capture_output=True,text=True,check=False)
    return r.returncode==0 and not r.stdout.strip()

def is_empty(value):
    return value is None or str(value).strip()==""

def write_report(env,features,run_settings):
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"A6_PILOT_READINESS_CHECKS_PRIVATE.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(("check","status","detail"));w.writerows(checks)
    passed=sum(status=="PASS" for _,status,_ in checks)
    failed=len(checks)-passed
    data={
      "technical_input_checks":"PASS" if failed==0 else "FAIL",
      "technical_passed":passed,"technical_failed":failed,
      "pilot_authorization":"HOLD",
      "research_holds":[{"gate":a,"reason":b} for a,b in holds],
      "environment":env,
      "model_features":features,
      "proposed_experiment":run_settings,
      "strict_limits":[
         "Static checks only; no code from original project was imported or executed.",
         "Real object rows, values, probabilities and grouping outputs are never exported.",
         "Pilot authorization remains HOLD regardless of technical check success.",
         "No 2014 published cluster result or algorithmic equivalence is claimed."
      ]
    }
    (OUT/"A6_PILOT_READINESS_PRIVATE.json").write_text(
       json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"\nTECHNICAL: {data['technical_input_checks']} — {passed} PASS / {failed} FAIL")
    print("PILOT AUTHORIZATION: HOLD — author/paper feature discrepancy and model-policy approval")
    print("PRIVATE reports:",OUT)
    return failed==0

def main():
    check("Official corpus CSV exists",INPUT.is_file(),INPUT)
    check("aneic-core fixed commit",commit(BASE/"aneic-core")==CORE_SHA,
          commit(BASE/"aneic-core"))
    check("aneic-scripts fixed commit",commit(BASE/"aneic-scripts")==SCRIPT_SHA,
          commit(BASE/"aneic-scripts"))
    check("Original core Git worktree clean",working_tree_clean(BASE/"aneic-core"),
          "no changes to author's checkout")
    check("Original scripts Git worktree clean",working_tree_clean(BASE/"aneic-scripts"),
          "no changes to author's checkout")
    all_present=all(p.is_file() for p in FILES.values())
    check("All five private compatibility modules present",all_present,
          ", ".join(k for k,v in FILES.items() if v.is_file()))
    rfile=BASE/"aneic-scripts/130317_01_mfm_sigma_1.0_a_2.0/run_mfm.py"
    check("Historical runner file present",rfile.is_file(),rfile)
    if not INPUT.is_file() or not all_present or not rfile.is_file():
        hold("Technical completeness","Missing a required input; cannot plan executable pilot")
        write_report({},[],{})
        return 1

    check("Official corpus SHA-256",sha(INPUT)==DATA_SHA,sha(INPUT))
    runner=rfile.read_text(encoding="utf-8")
    expected_tokens={
     "Site excluded": "'drop_feats' : ['Site']",
     "No object rows excluded": "'drop_objs' : []",
     "Historical K scan 2 to 10": "'K' : [2,3,4,5,6,7,8,9,10]",
     "Historical a=2 prior": "'a' : 2.0",
     "Historical sigma=1": "'sigma' : 1.0",
     "Historical random seed=1": "'seed' : 1",
     "Historical min_restarts=100": "'min_restarts' : 100",
     "Historical max_restarts=500": "'max_restarts' : 500",
    }
    for name, token in expected_tokens.items():
        check("Runner: "+name,token in runner,"fixed source token")

    with INPUT.open(encoding="utf-8-sig",newline="") as fh:
        reader=csv.reader(fh)
        header=next(reader)
        rows=list(reader)
    size_ok=(len(rows)==162 and len(header)==34 and
             all(len(row)==34 for row in rows))
    check("Official source has 162 rows and 34 fields",size_ok,
          f"rows={len(rows)}, fields={len(header)}")
    check("Identifier Key and label Site are first fields",
          header[:2]==["Key","Site"],str(header[:2]))
    ids=[row[0] for row in rows if row]
    check("Key is unique and non-empty",
          len(ids)==162 and len(set(ids))==162 and all(ids),
          "162 unique record IDs (identities not exported)")
    sites={row[1] for row in rows if len(row)>1}
    check("Five Site labels",len(sites)==5,f"count={len(sites)}")
    missing=sum(is_empty(v) for row in rows for v in row[2:])
    check("1931 missing model-feature cells",missing==1931,missing)
    numeric=all(is_empty(row[i]) or is_number(row[i])
                for row in rows for i in range(2,14))
    check("12 candidate numeric columns parse",numeric,"columns 3..14")
    check("20 remaining categorical columns",
          len(header[14:])==20,len(header[14:]))
    feature_cols=header[2:]
    check("Exactly 32 predictors after Key and Site are excluded",
          len(feature_cols)==32,len(feature_cols))
    features=[{"field":name,"type":"numeric_candidate" if i<12 else "categorical_candidate"}
              for i,name in enumerate(feature_cols)]
    # Only column names in private JSON, not values or individual observations.

    from importlib import metadata
    packages={}
    for pkg in ("numpy","pandas","scipy"):
        try: packages[pkg]=metadata.version(pkg)
        except metadata.PackageNotFoundError: packages[pkg]="NOT INSTALLED"
    check("Required modern smoke environment packages available",
          all(v!="NOT INSTALLED" for v in packages.values()),packages)
    check("Running in a dedicated venv",
          sys.prefix!=sys.base_prefix,"use A6 .venv, not global Python")
    version_hashes={name:sha(path) for name,path in FILES.items()}
    print("INFO | Private compatibility module SHA-256s recorded (no source copied)")
    compat={k:v.read_text(encoding="utf-8") for k,v in FILES.items()}
    check("Aligned return preserved in compat-v4/v5",
          all("return q_, g, L + [L_], g0" in compat[k]
              for k in ("compat-v4","compat-v5")),
          "return-state policy aligned")
    hist="if it > 1 and ((dL < eps) or it > max_iter):"
    alt="if it > 1 and (((0 <= dL) and (dL < eps)) or it >= max_iter):"
    check("Historical stop still present in compat-v4",hist in compat["compat-v4"],
          "historical policy")
    check("Candidate stop present in compat-v5",alt in compat["compat-v5"],
          "alternative policy; not validated as optimal")
    check("V4-to-V5 only changes stop predicate",
          compat["compat-v4"].replace(hist,alt,1)==compat["compat-v5"],
          "exact single difference across local copies")
    check("V3-to-V4 only changes return expression",
          compat["compat-v3"].replace("return q, g, L, g0",
                                     "return q_, g, L + [L_], g0",1)==compat["compat-v4"],
          "output phase alignment only")

    # Explicit research/method gates — no auto-approval.
    hold("Paper-versus-code features",
         "Paper reports 33; fixed runner uses 32 after excluding Site; not reconciled")
    hold("Method semantics",
         "Confirm whether experimental pilot targets historical control, aligned-output "
         "control, or candidate stopping policy; do not conflate these runs")
    hold("Study comparison",
         "Define comparison outputs and checkpoints before any object-level real-data fitting")
    hold("Ethics and permission",
         "Keep CC BY-SA corpus local and museum imagery excluded; confirm reuse and reporting plan")
    hold("Pilot approval",
         "Separate explicit go/no-go authorization required before actual real-data fitting")

    settings={
       "state":"PROPOSAL_ONLY",
       "suggested_first_k":2,
       "suggested_first_seed":17,
       "suggested_max_iter":3,
       "suggested_restart_count":1,
       "prohibited_without_approval":"Full original K=2..10 × 100..500 restarts",
       "variant_choices":["historical","aligned_return","candidate_stop"],
       "required_artifacts":[
           "input and source SHA256","feature-order manifest",
           "software versions","selected variant and exact patch SHA256",
           "seed, K, bounds","objective sequence and stop reason",
           "output state-alignment QC","private output paths"
       ]
    }
    env={"python":sys.version.split()[0],"executable":sys.executable,
         "packages":packages,"core_commit":CORE_SHA,"script_commit":SCRIPT_SHA,
         "official_csv_sha256":DATA_SHA,"private_compat_hashes":version_hashes}
    return 0 if write_report(env,features,settings) else 1

def is_number(value):
    try:
        return math.isfinite(float(value))
    except (ValueError,TypeError):
        return False

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as ex:
        check("Unexpected readiness audit exception",False,type(ex).__name__+": "+str(ex))
        hold("Technical exception","Readiness checks interrupted")
        write_report({},[],{})
        raise

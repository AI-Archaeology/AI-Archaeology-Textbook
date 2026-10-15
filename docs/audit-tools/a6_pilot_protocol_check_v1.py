#!/usr/bin/env python3
"""Read-only A6 proposed pilot protocol verifier. NEVER runs or imports EM.

Usage: <A6 private venv python> audit-tools/a6_pilot_protocol_check_v1.py
All reports are placed under ignored downloads/private-review/a6-ivories/.
A technical PASS NEVER changes protocol.authorization=HOLD.
"""
from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from importlib import metadata

PROJECT=Path.cwd()
POLICY=PROJECT/"audit-tools/a6_pilot_protocol_v1.json"
PRIVATE=PROJECT/"downloads/private-workflow/a6-reproduction"
OUT=PROJECT/"downloads/private-review/a6-ivories"
checks=[]

def check(name,passed,detail):
    s="PASS" if bool(passed) else "FAIL"
    checks.append((name,s,str(detail)))
    print(f"{s} | {name} | {detail}")

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def head(path):
    p=subprocess.run(["git","-C",str(path),"rev-parse","HEAD"],
                     capture_output=True,text=True,check=False)
    return p.stdout.strip() if p.returncode==0 else None

def pristine(path):
    p=subprocess.run(["git","-C",str(path),"status","--porcelain"],
                     capture_output=True,text=True,check=False)
    return p.returncode==0 and not p.stdout.strip()

def run():
    if len(sys.argv)!=1:
        raise ValueError("No arguments; run from the textbook project root")
    p=json.loads(POLICY.read_text(encoding="utf-8"))
    check("Protocol explicitly on HOLD",p["authorization"]=="HOLD","cannot authorize fitting")
    check("Proposal is not a result",p["status"]=="PROPOSED_NOT_AUTHORIZED",p["status"])
    check("Private output required",p["pilot_primary"]["output"]=="PRIVATE_ONLY",p["pilot_primary"]["output"])
    check("Primary uses aligned-return historical-stop compat-v4",
          p["pilot_primary"]["implementation"]=="compat-v4",p["pilot_primary"]["semantics"])
    check("Sensitivity is separate alternative",
          p["sensitivity"]["implementation"]=="compat-v5" and
          p["sensitivity"]["run_only_after_primary_review"],"not the historical implementation")
    check("Pilot limited to K=2, one seed and one initialization",
          p["pilot_primary"]["K"]==2 and
          p["pilot_primary"]["seed"]==17 and
          p["pilot_primary"]["proposed_initializations"]==1,
          "proposed diagnostic only, not historical experiment")
    check("Prior b remains explicitly unresolved",
          p["pilot_primary"]["precision_prior_b"].startswith("HOLD_"),
          "do not guess the source prior construction")
    check("Original feature discrepancy explicitly unresolved",
          "OPEN_" in p["input_contract"]["paper_feature_discrepancy"],
          p["input_contract"]["paper_feature_discrepancy"])
    check("At least six research holds",
          len(p["preflight_holds"])>=6,len(p["preflight_holds"]))
    for key,folder in [("core_commit","aneic-core"),("scripts_commit","aneic-scripts")]:
        path=PRIVATE/folder
        check(folder+" fixed source commit",head(path)==p["source"][key],head(path))
        check(folder+" source checkout pristine",pristine(path),"no local changes")
    file=PROJECT/p["source"]["corpus_relative_path"]
    check("Private official corpus exists",file.is_file(),p["source"]["corpus_relative_path"])
    if file.is_file():
        check("Corpus SHA-256 fixed",digest(file)==p["source"]["corpus_sha256"],digest(file))
        with file.open(encoding="utf-8-sig",newline="") as h:
            reader=csv.reader(h)
            header=next(reader)
            count=missing=0
            ids=set()
            widths_ok=True
            for row in reader:
                count+=1
                widths_ok=widths_ok and len(row)==34
                ids.add(row[0])
                missing+=sum(v.strip()=="" for v in row[2:])
        inp=p["input_contract"]
        check("162 rows and 34 original columns",
              count==inp["rows"] and len(header)==inp["source_columns"] and widths_ok,
              f"{count} x {len(header)}")
        check("Key and Site in original order",
              header[:2]==["Key","Site"],"index=Key, excluded label=Site")
        check("Source has 32 candidate predictors",
              len(header[2:])==inp["selected_feature_count"],len(header[2:]))
        check("Keys distinct without emitting identifiers",len(ids)==count,len(ids))
        check("Missing cells remain 1931",
              missing==inp["missing_feature_cells"],missing)
    hashes={}
    for ver in ("compat-v3","compat-v4","compat-v5"):
        f=PRIVATE/ver/"src/aneic/mfm.py"
        check(ver+" private module exists",f.is_file(),ver)
        if f.is_file():hashes[ver]=digest(f)
    if len(hashes)==3:
        old=(PRIVATE/"compat-v3/src/aneic/mfm.py").read_text(encoding="utf-8")
        aligned=(PRIVATE/"compat-v4/src/aneic/mfm.py").read_text(encoding="utf-8")
        candidate=(PRIVATE/"compat-v5/src/aneic/mfm.py").read_text(encoding="utf-8")
        check("Only one return-line change from v3 to v4",
              old.replace("return q, g, L, g0",
                          "return q_, g, L + [L_], g0",1)==aligned,"verified text equality")
        check("Only one stop-rule change from v4 to v5",
              aligned.replace("if it > 1 and ((dL < eps) or it > max_iter):",
                        "if it > 1 and (((0 <= dL) and (dL < eps)) or it >= max_iter):",1)==candidate,
              "verified text equality")
    versions={"python":sys.version.split()[0]}
    for name in ("numpy","pandas","scipy"):
        try:versions[name]=metadata.version(name)
        except metadata.PackageNotFoundError:versions[name]="NOT_INSTALLED"
    check("Dedicated virtualenv selected",sys.prefix!=sys.base_prefix,"no global Python")
    check("Scientific package metadata recorded",
          all(versions.get(n)!="NOT_INSTALLED" for n in ("numpy","pandas","scipy")),versions)
    # No fit, original import, object rows, or cluster outputs!
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"A6_PROTOCOL_FINALIZATION_CHECKS_PRIVATE.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerow(["check","status","detail"])
        w.writerows(checks)
    passes=sum(s=="PASS" for _,s,_ in checks)
    failures=len(checks)-passes
    summary={
        "technical_status":"PASS" if not failures else "FAIL",
        "technical_passes":passes,"technical_failures":failures,
        "pilot_authorization":"HOLD",
        "protocol_sha256":digest(POLICY),
        "fixed_source_sha256":p["source"]["corpus_sha256"],
        "private_compat_sha256":hashes,
        "environment":versions,
        "unresolved_decisions":p["preflight_holds"],
        "not_executed":["EM fit","real-data model evaluation",
                        "historical K/restart grid","object-wise exports"]
    }
    (OUT/"A6_PROTOCOL_FINALIZATION_PRIVATE.json").write_text(
        json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"\nTECHNICAL: {summary['technical_status']} — {passes} PASS / {failures} FAIL")
    print("PILOT AUTHORIZATION: HOLD — no real-data EM was run")
    print("PRIVATE reports:",OUT)
    return int(failures!=0)

if __name__=="__main__":
    try:sys.exit(run())
    except Exception as ex:
        print("FAIL | Protocol verifier exception |",type(ex).__name__,str(ex))
        raise

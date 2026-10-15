#!/usr/bin/env python3
"""A6: minimally patched private author-module copy and toy behavior comparison.

Requires Python 3, NumPy and pandas inside the dedicated A6 private venv.
Does NOT read genuine ivory data, run EM, train models, or modify original Git clones.
Only patches three obsolete pandas categorical/groupby interfaces in mfm.py.
"""
from __future__ import annotations
import argparse
import csv
import difflib
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys

CORE_SHA = "43a394f3a2409f2918d38f9d3cfc6dd5472970c1"
PATCH_MAP = [
    (
        "pd.core.categorical.Categorical.from_array(np.asarray(series))",
        "pd.Categorical(np.asarray(series))",
    ),
    (
        "np.eye(len(cat.levels)).take(cat.labels, axis=0)",
        "np.eye(len(cat.categories)).take(np.maximum(cat.codes, 0), axis=0)",
    ),
    ("dummy_cols = cat.levels", "dummy_cols = cat.categories"),
    (
        "((np.log(rho[k]) * cat).sum(1, level=0)).sum(1)",
        "((np.log(rho[k]) * cat).T.groupby(level=0).sum().T).sum(axis=1)",
    ),
]
BASE = Path("downloads/private-workflow/a6-reproduction")
OUT = Path("downloads/private-review/a6-ivories")
checks: list[dict[str,str]] = []

def check(label, result, detail):
    status = "PASS" if bool(result) else "FAIL"
    checks.append({"check": label, "status": status, "detail": str(detail)})
    print(f"{status} | {label} | {detail}")

def sha256(bs: bytes) -> str:
    return hashlib.sha256(bs).hexdigest()

def approx(a, b, tol=1e-10):
    return math.isclose(float(a), float(b), abs_tol=tol, rel_tol=tol)

def git_head(path):
    r = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                       capture_output=True, text=True, check=False)
    return r.stdout.strip() if r.returncode == 0 else None

def save_report(meta):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT/"A6_AUTHOR_TOY_EQ_CHECKS_PRIVATE.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, ["check", "status", "detail"])
        w.writeheader(); w.writerows(checks)
    success = sum(x["status"] == "PASS" for x in checks)
    failure = sum(x["status"] == "FAIL" for x in checks)
    meta.update({"passed": success, "failed": failure,
                 "status": "PASS" if failure == 0 else "FAIL",
                 "limitations": [
                    "Author source copied privately with only four textual API substitutions.",
                    "E/M step and historical MAP objective NOT executed.",
                    "Toy tests demonstrate selected source functions only, not full equivalence.",
                    "No genuine ivory record read or published.",
                    "Source patch.diff retained only in private directory."
                 ]})
    (OUT/"A6_AUTHOR_TOY_EQ_REPORT_PRIVATE.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"\nOVERALL: {meta['status']} — {success} PASS / {failure} FAIL")
    print("PRIVATE results:", OUT)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--core", default=str(BASE/"aneic-core"))
    parser.add_argument("--private-copy", default=str(BASE/"compat-v1"))
    args=parser.parse_args()
    core=Path(args.core).resolve()
    dest=Path(args.private_copy).resolve()
    source=core/"src/aneic/mfm.py"
    original=source.read_text(encoding="utf-8")
    check("Fixed original commit", git_head(core)==CORE_SHA, git_head(core))
    # Refuse to patch a checkout that has local edits to the actual file.
    r=subprocess.run(["git","-C",str(core),"diff","--quiet","--","src/aneic/mfm.py"],
                     check=False)
    check("Original mfm.py has no unstaged modifications", r.returncode==0, r.returncode)
    staged=subprocess.run(["git","-C",str(core),"diff","--cached","--quiet","--","src/aneic/mfm.py"],
                          check=False)
    check("Original mfm.py has no staged modifications", staged.returncode==0, staged.returncode)
    if any(x["status"]=="FAIL" for x in checks):
        save_report({"phase":"source validation"});sys.exit(1)

    modified=original
    for old,new in PATCH_MAP:
        n=modified.count(old)
        check("Unique original pattern: "+old[:46], n==1, "matches "+str(n))
        if n==1: modified=modified.replace(old,new,1)
    if any(x["status"]=="FAIL" for x in checks):
        save_report({"phase":"patch preflight"});sys.exit(1)
    # A PRIVATE working copy, not a new Git repository or mutation of author checkout.
    compat_file=dest/"src/aneic/mfm.py"
    dest.mkdir(parents=True, exist_ok=True)
    compat_file.parent.mkdir(parents=True, exist_ok=True)
    if compat_file.exists():
        existing=compat_file.read_text(encoding="utf-8")
        check("Existing compatibility copy matches expected patch",
              existing==modified, "no overwrite performed")
        if existing!=modified:
            save_report({"phase":"copy conflict"});sys.exit(1)
    else:
        compat_file.write_text(modified,encoding="utf-8")
        check("Compatibility copy created outside original checkout", True, str(compat_file))
    diff="".join(difflib.unified_diff(
       original.splitlines(keepends=True), modified.splitlines(keepends=True),
       fromfile="aneic-core/original/mfm.py",tofile="PRIVATE/compat-v1/mfm.py"))
    (dest/"A6_PATCH_DIFF_PRIVATE.patch").write_text(diff,encoding="utf-8")
    check("Only four authorized substitutions", modified!=original and diff.count("\n@@")>=1,
          "patch stored privately")
    import numpy as np
    import pandas as pd
    spec=importlib.util.spec_from_file_location("aneic_a6_compat_toy",compat_file)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # FOUR COMPLETELY INVENTED observations, never a real site/object identifier.
    examples=pd.DataFrame({"x":[0.0,2.0,np.nan,1.0],
                           "cat":pd.Series(["A","B","A",None],dtype="object")},
                          index=["toy-1","toy-2","toy-3","toy-4"])
    ind=module.get_indicator(examples["cat"])
    check("Historical get_indicator adapted: correct toy categories",
          list(ind.columns)==["A","B"] and approx(ind.loc["toy-1","A"],1)
          and approx(ind.loc["toy-2","B"],1),list(ind.columns))
    check("Historical get_indicator adapted: missing is NaN",
          ind.loc["toy-4"].isna().all(),"missing is not a third observed category or zero")
    cat=pd.concat([ind],axis=1,keys=["cat"])
    real=examples[["x"]]
    mu=pd.DataFrame({0:[0.0],1:[2.0]},index=["x"])
    precision=pd.DataFrame({0:[1.0],1:[1.0]},index=["x"])
    rho=pd.DataFrame({0:[.8,.2],1:[.3,.7]},index=cat.columns)
    pi=pd.Series([.6,.4],index=[0,1])
    # Run selected ORIGINAL author functions, with minimal API patches.
    log_joint=module._log_pxyz(real,cat,mu,precision,rho,pi)
    check("Author log-joint has four rows and two states",
          log_joint.shape==(4,2),str(log_joint.shape))
    posterior=np.exp(log_joint.to_numpy(dtype=float))
    posterior/=posterior.sum(axis=1,keepdims=True)
    check("Author log-joint yields normalized posteriors",
          bool(np.all(np.isfinite(posterior)) and np.allclose(posterior.sum(axis=1),1)),
          "4 toy responsibilities sum to one")
    def pdf(x,m):
        return math.exp(-.5*(x-m)**2)/math.sqrt(2*math.pi)
    expected=(.6*pdf(0,0)*.8)/(.6*pdf(0,0)*.8+.4*pdf(0,2)*.3)
    check("Author E-step factors agree with independent first-row calculation",
          approx(posterior[0,0],expected),f"author={posterior[0,0]:.12f}; reference={expected:.12f}")
    neutral_x=(.6*.8)/(.6*.8+.4*.3)
    check("Absent numerical observation contributes neutral likelihood",
          approx(posterior[2,0],neutral_x),f"author={posterior[2,0]:.12f}; expected={neutral_x:.12f}")
    neutral_cat=(.6*pdf(1,0))/(.6*pdf(1,0)+.4*pdf(1,2))
    check("Absent categorical observation contributes neutral likelihood",
          approx(posterior[3,0],neutral_cat),f"author={posterior[3,0]:.12f}; expected={neutral_cat:.12f}")
    check("Original git revision remains fixed after run",
          git_head(core)==CORE_SHA,git_head(core))
    save_report({"phase":"toy source behavior","source_sha256":sha256(original.encode()),
                 "patched_sha256":sha256(modified.encode()),
                 "python":sys.version.split()[0],
                 "numpy":np.__version__,"pandas":pd.__version__,
                 "patch_substitutions":len(PATCH_MAP)})
    sys.exit(0 if all(x["status"]=="PASS" for x in checks) else 1)

if __name__=="__main__":
    try: main()
    except Exception as err:
        check("Unexpected author-function compatibility exception",False,type(err).__name__+": "+str(err))
        save_report({"phase":"exception"})
        raise

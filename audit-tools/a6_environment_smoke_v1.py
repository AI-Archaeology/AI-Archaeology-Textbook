#!/usr/bin/env python3
"""A6 V1 isolated environment and input-encoding smoke check.

Does not import or execute ANEIC's historical source, train a model, or
write original observations. Run with a dedicated venv Python interpreter.
Usage:
 downloads/private-workflow/a6-reproduction/.venv/bin/python \
   audit-tools/a6_environment_smoke_v1.py \
   downloads/official/levantine_corpus_gansell.csv
"""
from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

APPROVED_SHA256 = "d52ed8033ad7304024e207e02117d2cc1b425da8799e582858dac8a6b0b90941"
OUTPUT = Path("downloads/private-review/a6-ivories")
checks = []
def report(label, passed, detail):
    checks.append(dict(check=label, status="PASS" if passed else "FAIL", detail=str(detail)))
    print(("PASS" if passed else "FAIL"), "|", label, "|", detail)

def missing(value):
    return value is None or str(value).strip() == ""

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: <venv_python> audit-tools/a6_environment_smoke_v1.py <local_official_CSV>")
    src = Path(sys.argv[1]).resolve(strict=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    isolated = sys.prefix != sys.base_prefix
    report("Independent Python virtual environment active", isolated, sys.prefix)
    digest = hashlib.sha256(src.read_bytes()).hexdigest()
    report("Approved source SHA-256", digest == APPROVED_SHA256, digest)

    try:
        import numpy as np
        import pandas as pd
    except ImportError as exc:
        report("NumPy and pandas importable", False, str(exc))
        write_reports()
        sys.exit(1)
    report("NumPy and pandas importable", True,
           "numpy " + np.__version__ + ", pandas " + pd.__version__)

    # Read CSV with explicit input column names, types and NA treatment.
    # This checks a MODERN data-reading baseline, not numerical equivalence
    # to the 2014 implementation.
    with src.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        rows = list(reader)
    shape_ok = len(rows) == 162 and len(header) == 34 and all(len(r) == 34 for r in rows)
    report("Raw source shape 162 x 34", shape_ok,
           f"{len(rows)} records, {len(header)} columns, all rows width 34: {shape_ok}")
    report("First two columns Key and Site", header[:2] == ["Key", "Site"], header[:2])
    blank_cells = sum(missing(c) for row in rows for c in row[2:])
    report("Model feature missing cells 1931", blank_cells == 1931, blank_cells)
    keys = [r[0] for r in rows]
    report("Key is unique and nonblank", len(keys) == len(set(keys)) and all(keys), len(keys))
    report("Five observed Site labels", len({r[1] for r in rows}) == 5, len({r[1] for r in rows}))
    numerical = rows and all(missing(r[i]) or can_float(r[i]) for r in rows for i in range(2, 14))
    report("12 candidate numeric columns parse", bool(numerical), "columns 3..14")

    # Toy one-hot test; do not use historical source records as examples.
    toy = pd.Series(["yes", "no", None, "yes"], dtype="string")
    indicator = pd.get_dummies(toy, dtype=float)
    if pd.isna(toy.iloc[2]):
        indicator.loc[2, :] = np.nan
    toy_ok = (set(indicator.columns) == {"no", "yes"}
              and float(indicator.iloc[0]["yes"]) == 1.0
              and float(indicator.iloc[1]["no"]) == 1.0
              and indicator.iloc[2].isna().all()
              and float(indicator.iloc[3]["yes"]) == 1.0)
    report("Toy categorical encoding preserves missingness", bool(toy_ok),
           "yes/no encoded; unobserved value remains NaN")

    # Toy numerical test: deliberately not the historical EM implementation.
    v = np.array([0.2, np.nan, 0.8], dtype=float)
    arithmetic_ok = np.isclose(np.nanmean(v), 0.5) and np.isnan(v[1])
    report("Toy numeric missingness preserved", bool(arithmetic_ok),
           "0.2 / missing / 0.8, no zero imputation")
    write_reports(np_version=np.__version__, pd_version=pd.__version__)

def can_float(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False

def write_reports(np_version=None, pd_version=None):
    import datetime
    with (OUTPUT / "A6_ENV_SMOKE_CHECKS_PRIVATE.csv").open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=["check", "status", "detail"])
        w.writeheader()
        w.writerows(checks)
    identity = {
        "python": sys.version.split()[0], "executable": sys.executable,
        "virtual_environment": sys.prefix != sys.base_prefix,
        "numpy": np_version, "pandas": pd_version,
        "platform": platform.platform(),
        "status": "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL",
        "passed": sum(c["status"] == "PASS" for c in checks),
        "failed": sum(c["status"] == "FAIL" for c in checks),
        "limitations": [
          "No historical code executed; no EM or clustering model run.",
          "Toy encoding test is not a behavioral-equivalence proof.",
          "Original source observations are not exported.",
          "Package versions are observed, not yet certified/pinned."
        ]
    }
    (OUTPUT / "A6_ENV_SMOKE_PRIVATE.json").write_text(
        json.dumps(identity, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\nOVERALL:", identity["status"], "—", identity["passed"],
          "PASS /", identity["failed"], "FAIL")
    print("PRIVATE reports:", OUTPUT)
    if identity["failed"]:
        sys.exit(1)

if __name__ == "__main__":
    main()

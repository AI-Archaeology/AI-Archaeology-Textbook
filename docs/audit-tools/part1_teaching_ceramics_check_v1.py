#!/usr/bin/env python3
"""Read-only audit of the 18-record SIMULATED ceramics teaching CSV (stdlib only).

This is NOT an audit of archaeological field data. Exit nonzero on failed checks.
Usage: python3 audit-tools/part1_teaching_ceramics_check_v1.py
"""
import csv
import io
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "data" / "teaching-ceramics-01"
FIELDS = [
    "artifact_id", "context_id", "fragment_part", "fabric",
    "surface_treatment", "rim_diameter_cm", "coarse_inclusion_flag",
    "surface_unrecorded_flag",
]
CHECKS = []

def check(label, passed, detail):
    CHECKS.append((label, bool(passed), str(detail)))
    print(("PASS" if passed else "FAIL") + " | " + label + " | " + str(detail))

def load_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        return list(rd.fieldnames or []), list(rd)

def main():
    header, rows = load_csv(FOLDER / "ceramics.csv")
    dict_fields, dictionary = load_csv(FOLDER / "data_dictionary.csv")
    check("Teaching CSV identity", len(rows) == 18 and header == FIELDS,
          f"{len(rows)} records / {len(header)} fields")
    check("Dictionary variables", [r["variable"] for r in dictionary] == FIELDS,
          f"{len(dictionary)} dictionary entries")
    check("Unique object IDs", len({r["artifact_id"] for r in rows}) == len(rows) and
          all(r["artifact_id"] for r in rows), "each record has unique nonempty artifact_id")
    check("Object IDs expected", {r["artifact_id"] for r in rows} ==
          {f"TC{i:03d}" for i in range(1, 19)}, "TC001-TC018")
    context_counts = Counter(r["context_id"] for r in rows)
    check("Six simulated contexts", context_counts ==
          {c: 3 for c in ("A01", "A02", "B01", "B02", "C01", "C02")},
          str(dict(context_counts)))
    part_counts = Counter(r["fragment_part"] for r in rows)
    check("Fragment-part frequencies", part_counts ==
          {"口沿": 9, "腹片": 6, "底部": 3}, str(dict(part_counts)))
    check("Fabric vocabulary", {r["fabric"] for r in rows} <= {"泥质", "夹砂"},
          str(dict(Counter(r["fabric"] for r in rows))))
    surface_counts = Counter(r["surface_treatment"] for r in rows)
    check("Surface frequencies", surface_counts ==
          {"素面": 8, "绳纹": 6, "磨光": 3, "未记录": 1},
          str(dict(surface_counts)))
    rim = [r for r in rows if r["fragment_part"] == "口沿"]
    other = [r for r in rows if r["fragment_part"] != "口沿"]
    check("Non-rim structural blanks", len(other) == 9 and
          all(r["rim_diameter_cm"] == "" for r in other),
          "9/9 non-rim fragments have blank rim diameter, not zero")
    def positive_number(x):
        try:
            return float(x) > 0
        except (ValueError, TypeError):
            return False
    check("Rim numeric values", len(rim) == 9 and
          all(positive_number(r["rim_diameter_cm"]) for r in rim),
          "9/9 rims have positive parseable diameter values")
    check("Rim unit", any(r["variable"] == "rim_diameter_cm" and
          "厘米" in r["allowed_values_or_unit"] for r in dictionary), "cm")
    check("No 0 imputation", all(r["rim_diameter_cm"] not in {"0", "0.0"} for r in rows),
          "No zero-coded rim diameter")
    check("Binary indicator domain", all(r[k] in {"0", "1"} for r in rows
          for k in ("coarse_inclusion_flag", "surface_unrecorded_flag")),
          "only 0/1")
    check("Visible coarse inclusion counts",
          Counter(r["coarse_inclusion_flag"] for r in rows) == {"0": 13, "1": 5},
          "0 is 'not recorded visible', NOT 'proven absent'")
    missed = [r for r in rows if r["surface_treatment"] == "未记录"]
    check("Unrecorded surface flag equivalence",
          len(missed) == 1 and all(
              (r["surface_treatment"] == "未记录") ==
              (r["surface_unrecorded_flag"] == "1") for r in rows),
          "one '未记录' case, exactly matches flag=1")
    check("Dictionary distinguishes missing vs none", any(
          r["variable"] == "surface_treatment" and "记录缺失" in r["missing_rule"]
          for r in dictionary), "未记录 is a documentation state")
    check("Dictionary specifies rim N/A", any(
          r["variable"] == "rim_diameter_cm" and "非口沿" in r["missing_rule"]
          for r in dictionary), "non-rim diameter not applicable")
    check("Dictionary coarse flag semantics", any(
          r["variable"] == "coarse_inclusion_flag" and "未记录到" in r["missing_rule"]
          for r in dictionary), "flag=0 not proof of absence")
    check("Dictionary provenance of simulation",
          any(r["variable"] == "context_id" and "虚构" in r["description_zh"]
              for r in dictionary), "contexts are simulated")
    print(f"RESULT | {sum(v for _, v, _ in CHECKS)} PASS / "
          f"{sum(not v for _, v, _ in CHECKS)} FAIL")
    print("SCOPE | Read-only simulated-data structural/semantic QA; "
          "NOT archaeological-data verification or model validation")
    return int(any(not v for _, v, _ in CHECKS))

if __name__ == "__main__":
    sys.exit(main())

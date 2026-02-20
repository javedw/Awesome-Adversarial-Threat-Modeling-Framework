#!/usr/bin/env python3
"""Enrich standards crosswalk by attempting to fetch MITRE ATT&CK techniques
and merge technique IDs into matching threat entries in the YAML crosswalk.

This script is conservative: it only adds technique IDs when the technique
name contains the threat name (case-insensitive) or vice-versa. It writes a
backup file before modifying the crosswalk.

Usage: python scripts/enrich_crosswalk.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from ruamel.yaml import YAML

MITRE_ENTERPRISE_URL = (
    "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
)


def fetch_mitre_json(url: str) -> dict | None:
    try:
        with urlopen(url, timeout=20) as resp:
            return json.load(resp)
    except (HTTPError, URLError) as e:
        print(f"Failed to fetch MITRE data: {e}")
        return None


def build_techniques_map(mitre_json: dict) -> dict:
    tech_map: dict = {}
    for obj in mitre_json.get("objects", []):
        if obj.get("type") in ("attack-pattern",):
            name = obj.get("name", "").lower()
            ext = obj.get("external_references", []) or []
            tid = None
            for er in ext:
                if er.get("source_name") == "mitre-attack" and er.get("external_id"):
                    tid = er.get("external_id")
                    break
            if tid:
                tech_map.setdefault(name, []).append(tid)
    return tech_map


def load_crosswalk(p: Path) -> list:
    yaml = YAML(typ="safe")
    with p.open("r") as f:
        return yaml.load(f)


def write_crosswalk(p: Path, data: list):
    yaml = YAML()
    yaml.default_flow_style = False
    backup = p.with_suffix(p.suffix + ".bak")
    p.rename(backup)
    with p.open("w") as f:
        yaml.dump(data, f)
    print(f"Wrote enriched crosswalk to {p} (backup at {backup})")


def enrich(crosswalk: list, tech_map: dict) -> int:
    added = 0
    # create simple reverse map of technique name tokens -> ids
    for entry in crosswalk:
        name = (entry.get("name") or "").lower()
        if not name:
            continue
        # try exact technique name match first
        for tech_name, ids in tech_map.items():
            if name in tech_name or tech_name in name:
                # merge ids into entry.mitre list
                mitre = entry.setdefault("mitre", []) or []
                for tid in ids:
                    if tid not in mitre:
                        mitre.append(tid)
                        added += 1
    return added


def main():
    repo_root = Path(__file__).parents[1]
    p = repo_root / "docs" / "crosswalks" / "standards_full_crosswalk.yaml"
    if not p.exists():
        print(f"Crosswalk not found at {p}")
        sys.exit(2)

    print("Fetching MITRE ATT&CK enterprise dataset...")
    mitre = fetch_mitre_json(MITRE_ENTERPRISE_URL)
    if mitre is None:
        print("Could not fetch MITRE dataset; aborting enrichment.")
        sys.exit(0)

    tech_map = build_techniques_map(mitre)
    print(f"Loaded {sum(len(v) for v in tech_map.values())} technique references.")

    cw = load_crosswalk(p)
    added = enrich(cw, tech_map)
    if added:
        write_crosswalk(p, cw)
        print(f"Added {added} new technique ID entries.")
    else:
        print("No new technique IDs were added.")


if __name__ == "__main__":
    main()

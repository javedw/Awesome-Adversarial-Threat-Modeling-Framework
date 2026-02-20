from pathlib import Path
from ruamel.yaml import YAML


def load_crosswalk():
    yaml = YAML(typ="safe")
    p = Path(__file__).parents[1] / "docs" / "crosswalks" / "standards_full_crosswalk.yaml"
    with p.open("r") as f:
        return yaml.load(f)


def test_injection_has_mitre_and_nist():
    data = load_crosswalk()
    thr = next((t for t in data if t.get("id") == "THR-001"), None)
    assert thr is not None
    assert "mitre" in thr and "T1190" in thr["mitre"]
    assert "nist" in thr and "controls" in thr["nist"] and "SI-10" in thr["nist"]["controls"]


def test_broken_auth_has_AC2():
    data = load_crosswalk()
    thr = next((t for t in data if t.get("id") == "THR-002"), None)
    assert thr is not None
    assert "nist" in thr and "controls" in thr["nist"] and "AC-2" in thr["nist"]["controls"]


def test_sensitive_data_exposure_has_T1567():
    data = load_crosswalk()
    thr = next((t for t in data if t.get("id") == "THR-003"), None)
    assert thr is not None
    assert "mitre" in thr and "T1567" in thr["mitre"]

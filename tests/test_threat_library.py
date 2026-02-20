import os
from aatmf_nonai.threat_library import ThreatLibrary


def test_load_yaml_and_find(tmp_path):
    lib = ThreatLibrary()
    sample = os.path.join(os.path.dirname(__file__), "fixtures", "sample_threats.yaml")
    lib.load_from_yaml(sample)

    # ensure entries loaded
    assert lib.get("THR-TEST-001") is not None
    assert lib.get("THR-TEST-002") is not None

    # find by standard
    found = lib.find_by_standard("nist_controls", "SI-10")
    assert any(t.id == "THR-TEST-001" for t in found)

    found2 = lib.find_by_standard("owasp", "A3")
    assert any(t.id == "THR-TEST-002" for t in found2)

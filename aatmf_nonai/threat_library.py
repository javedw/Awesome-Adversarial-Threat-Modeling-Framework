"""Threat library and mappings to external standards.

Provides a richer Threat model with utilities to load machine-readable
threat catalogs (YAML/JSON), search by mapping (MITRE/OWASP/NIST/ISM),
and export simple summaries.
"""
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from pathlib import Path

try:
    import ruamel.yaml as ry
    _YAML = ry.YAML
except Exception:
    _YAML = None


@dataclass
class Threat:
    id: str
    name: str
    description: str
    severity: str = "medium"  # low, medium, high, critical
    mappings: Dict[str, List[str]] = None  # e.g., {"mitre": ["T1234"], "owasp": ["A1"]}

    def to_dict(self) -> Dict:
        d = asdict(self)
        if d.get("mappings") is None:
            d["mappings"] = {}
        return d


class ThreatLibrary:
    """In-memory catalog of Threat entries with helper methods."""

    def __init__(self):
        self._threats: Dict[str, Threat] = {}

    def add(self, threat: Threat):
        self._threats[threat.id] = threat

    def get(self, tid: str) -> Optional[Threat]:
        return self._threats.get(tid)

    def list(self) -> List[Threat]:
        return list(self._threats.values())

    def find_by_standard(self, standard: str, identifier: str) -> List[Threat]:
        """Return threats that map to a given standard identifier.

        Example: find_by_standard('owasp', 'A1')
        """
        out = []
        for t in self._threats.values():
            if not t.mappings:
                continue
            vals = t.mappings.get(standard.lower(), [])
            if identifier in vals:
                out.append(t)
        return out

    def search_by_name(self, term: str) -> List[Threat]:
        term_l = term.lower()
        return [t for t in self._threats.values() if term_l in t.name.lower() or term_l in (t.description or "").lower()]

    def load_from_yaml(self, path: str):
        """Load threats from a YAML file. The file should contain a top-level list of threat objects."""
        if _YAML is None:
            raise RuntimeError("ruamel.yaml is required to load YAML. Add ruamel.yaml to requirements.txt")
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(path)
        yaml = _YAML(typ="safe")
        with p.open("r") as fh:
            data = yaml.load(fh)
        if not isinstance(data, list):
            raise ValueError("Threat YAML must be a list of threat objects")
        for entry in data:
            tid = entry.get("id")
            if not tid:
                continue
            t = Threat(
                id=tid,
                name=entry.get("name", ""),
                description=entry.get("description", ""),
                severity=entry.get("severity", "medium"),
                mappings=entry.get("mappings", {}),
            )
            self.add(t)

    def to_summary(self) -> List[Dict]:
        return [t.to_dict() for t in self.list()]


def default_library() -> ThreatLibrary:
    """Return a pre-populated library of common web/application threats (improved).

    The mappings are illustrative; teams should replace entries with canonical
    identifiers for their organization.
    """
    lib = ThreatLibrary()

    lib.add(Threat(
        id="THR-001",
        name="Injection (SQL/Command/Template)",
        description="Improper input handling leads to execution of attacker-controlled code or queries.",
        severity="high",
        mappings={"owasp": ["A1"], "cwe": ["CWE-89"], "mitre": ["T1190", "T1059", "T1203"], "nist_controls": ["SI-10","SI-2"], "stride": ["Tampering", "Elevation"], "pasta_phase": ["Threat Analysis"], "australian_ism": ["Secure-Configuration","Patch-Management"], "essential_eight": ["Patch Applications","Application Whitelisting"]}
    ))

    lib.add(Threat(
        id="THR-002",
        name="Broken Authentication & Session Management",
        description="Weak authentication or session handling allows actor impersonation.",
        severity="high",
        mappings={"owasp": ["A2"], "cwe": ["CWE-287"], "mitre": ["T1078","T1110","T1531"], "nist_controls": ["AC-2", "AC-7", "IA-5"], "stride": ["Spoofing"], "pasta_phase": ["Attack Modeling"], "australian_ism": ["Identity-and-Access-Management","MFA"], "essential_eight": ["Multi-factor Authentication","Restrict Admin Privileges"]}
    ))

    lib.add(Threat(
        id="THR-003",
        name="Sensitive Data Exposure",
        description="Inadequate protection of data at rest or in transit leading to disclosure.",
        severity="high",
        mappings={"owasp": ["A3"], "cwe": ["CWE-200"], "nist_controls": ["SC-13", "MP-2", "SC-8"], "australian_ism": ["Data-Protection","Encryption"], "stride": ["Information Disclosure"], "pasta_phase": ["Threat Analysis"], "essential_eight": ["Backups","Patch Applications"]}
    ))

    lib.add(Threat(
        id="THR-004",
        name="Security Misconfiguration",
        description="Default or insecure configuration that increases attack surface.",
        severity="medium",
        mappings={"owasp": ["A6"], "cwe": ["CWE-16"], "nist_controls": ["CM-2", "CM-6"], "australian_ism": ["Config-Management"], "stride": ["Tampering", "Repudiation"], "pasta_phase": ["Design Analysis"]}
    ))

    lib.add(Threat(
        id="THR-005",
        name="Supply Chain Compromise",
        description="Third-party or upstream components are compromised, affecting trust.",
        severity="critical",
        mappings={"nist_controls": ["SA-12", "SR-3"], "mitre": ["T1195"], "australian_ism": ["Supply-Chain"], "stride": ["Tampering"], "pasta_phase": ["Supply Chain Analysis"]}
    ))

    # Additional high-quality entries with conservative, reviewable mappings
    lib.add(Threat(
        id="THR-006",
        name="Cross-Site Scripting (XSS)",
        description="User-controllable input is rendered without proper encoding, allowing script injection into other users' browsers.",
        severity="high",
        mappings={"owasp": ["A7"], "cwe": ["CWE-79"], "nist_controls": ["SI-10"], "mitre": ["T1059"], "stride": ["Tampering", "Information Disclosure"], "pasta_phase": ["Attack Modeling"]}
    ))

    lib.add(Threat(
        id="THR-007",
        name="Cross-Site Request Forgery (CSRF)",
        description="Lack of request validation allows attackers to perform actions on behalf of authenticated users.",
        severity="medium",
        mappings={"owasp": ["A10"], "cwe": ["CWE-352"], "nist_controls": ["AC-8"], "mitre": [], "stride": ["Spoofing", "Tampering"], "pasta_phase": ["Attack Modeling"]}
    ))

    lib.add(Threat(
        id="THR-008",
        name="Server-Side Request Forgery (SSRF)",
        description="Attacker can cause the server to make arbitrary requests, potentially accessing internal services.",
        severity="high",
        mappings={"owasp": ["A5"], "cwe": ["CWE-918"], "nist_controls": ["SC-7", "SC-8"], "mitre": ["T1210"], "stride": ["Tampering"], "pasta_phase": ["Attack Modeling"]}
    ))

    lib.add(Threat(
        id="THR-009",
        name="Remote Code Execution (RCE)",
        description="Vulnerabilities that allow attacker-supplied code to execute on the host.",
        severity="critical",
        mappings={"cwe": ["CWE-94"], "nist_controls": ["SI-3", "SI-10"], "mitre": ["T1203"], "stride": ["Tampering", "Execution"], "pasta_phase": ["Attack Modeling"]}
    ))

    lib.add(Threat(
        id="THR-004",
        name="Security Misconfiguration",
        description="Default or insecure configuration that increases attack surface.",
        severity="medium",
        mappings={
            "owasp": ["A6"],
            "cwe": ["CWE-16"],
            "nist_controls": ["CM-2", "CM-6", "CM-7"],
            "australian_ism": ["Config-Management","Secure-Deployment"],
            "stride": ["Tampering", "Repudiation"],
            "pasta_phase": ["Design Analysis"],
            "essential_eight": ["Secure Configuration of Applications","Patch Applications"],
        }
    ))

    lib.add(Threat(
        id="THR-005",
        name="Supply Chain Compromise",
        description="Third-party or upstream components are compromised, affecting trust.",
        severity="critical",
        mappings={
            "nist_controls": ["SA-12", "SR-3", "SA-9"],
            "mitre": ["T1195","T1584"],
            "australian_ism": ["Supply-Chain-Risk-Management"],
            "stride": ["Tampering"],
            "pasta_phase": ["Supply Chain Analysis"],
            "essential_eight": ["Patch Applications","Restrict Admin Privileges"],
        }
    ))

    lib.add(Threat(
        id="THR-006",
        name="Cross-Site Scripting (XSS)",
        description="User-controllable input is rendered without proper encoding, allowing script injection into other users' browsers.",
        severity="high",
        mappings={
            "owasp": ["A7"],
            "cwe": ["CWE-79"],
            "nist_controls": ["SI-10","SC-7","SC-8"],
            "mitre": ["T1059","T1055"],
            "stride": ["Tampering", "Information Disclosure"],
            "pasta_phase": ["Attack Modeling"],
            "australian_ism": ["Secure-Coding","Input-Validation"],
            "essential_eight": ["User Application Hardening","Secure Configuration of Applications"],
        }
    ))

    # Note: mappings use families or representative ATT&CK technique IDs where applicable.
    # Teams should expand mappings with organization-specific canonical IDs (e.g., NIST SP800-53 control numbers).

    return lib


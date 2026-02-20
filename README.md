# Awesome Adversarial Threat Modeling Framework (AATMF) — v1.0

A standards-aligned Threat Modeling Framework (non-AI) focused on mapping threats, controls and mitigations to NIST, OWASP, MITRE ATT&CK and the Australian ISM / Essential Eight.

This repository is a template scaffold to help security teams model attack surfaces, enumerate threat catalogs, compute risk scores, and produce actionable remediation reports.

See the `aatmf_nonai` package for core modules and `docs/` for standards crosswalks.

## Quickstart

Install requirements and run a quick example:

```bash
python -m pip install -r requirements.txt
python -m aatmf_nonai.cli generate-report examples/sample_system.yaml -o report.md
```

## License
MIT — see LICENSE

## Diagram

See `docs/diagrams/mappings_diagram.mmd` for a Mermaid diagram that shows how STRIDE, PASTA, DREAD and standards (MITRE/NIST/OWASP) tie together.

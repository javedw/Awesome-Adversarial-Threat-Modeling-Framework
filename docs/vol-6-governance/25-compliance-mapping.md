# Part 25: Compliance and Standards Mapping

## EU AI Act

| Milestone | Date | AATMF Relevance |
|:---|:---|:---|
| Prohibited practices effective | February 2, 2025 | T8 (social scoring, manipulation), T15 (biometric categorization) |
| GPAI obligations | August 2, 2025 | T6 (training data), T13 (supply chain transparency) |
| Full high-risk requirements | August 2, 2026 | All tactics — conformity assessment requires threat modeling |
| Maximum fine | €35M or 7% global turnover | |

### AATMF Coverage for EU AI Act Compliance

| EU AI Act Requirement | AATMF Mapping |
|:---|:---|
| Risk management system (Art. 9) | AATMF-R v3 scoring, Parts 24–25 |
| Data governance (Art. 10) | T6, T12 detection and mitigation |
| Technical documentation (Art. 11) | Full framework documentation |
| Transparency (Art. 13) | T7, T8 output validation |
| Human oversight (Art. 14) | T15 human workflow controls |
| Robustness (Art. 15) | T1–T5 resilience testing |
| Post-market monitoring (Art. 72) | Detection engineering (Part 19) |

## OWASP LLM Top 10 2025

| OWASP | Description | AATMF Primary | AATMF Secondary |
|:---|:---|:---|:---|
| LLM01 | Prompt Injection | T1, T2 | T3, T9 |
| LLM02 | Sensitive Information Disclosure | T10 | T7 |
| LLM03 | Supply Chain Vulnerabilities | T13 | T14 |
| LLM04 | Data and Model Poisoning | T6 | T12 |
| LLM05 | Improper Output Handling | T7 | T8 |
| LLM06 | Excessive Agency | T11 | T5 |
| LLM07 | System Prompt Leakage | T1 | T4 |
| LLM08 | Vector and Embedding Weaknesses | T12 | T10 |
| LLM09 | Misinformation | T8 | T15 |
| LLM10 | Unbounded Consumption | T14 | T5 |

## MITRE ATLAS v4.6.0 (October 2025)

ATLAS v4.6.0 added 14 new agentic AI techniques, bringing the total to 15 tactics, 66 techniques, and 46 sub-techniques. AATMF v3 provides finer-grained coverage:

| Comparison | MITRE ATLAS | AATMF v3 |
|:---|:---:|:---:|
| Tactics | 15 | 15 |
| Techniques | 66 | 240 |
| Sub-techniques | 46 | — |
| Attack procedures | — | 2,152+ |
| Prompts | — | 4,980+ |
| Risk scoring | No | Yes (AATMF-R v3) |

AATMF is designed to be complementary to ATLAS, not competitive. ATLAS provides breadth across the ML lifecycle; AATMF provides depth on adversarial attack techniques with executable procedures.

## NIST AI RMF / Cyber AI Profile (IR 8596)

The preliminary draft (December 2025) establishes control overlays for AI systems. AATMF maps to NIST functions:

| NIST Function | AATMF Coverage |
|:---|:---|
| GOVERN | Volume VI (Parts 24–26) |
| MAP | Part 3 (Architecture), Part 24 (Risk Management) |
| MEASURE | Part 2 (AATMF-R v3), Part 19 (Detection) |
| MANAGE | Parts 20–23 (Mitigation, IR, Red/Blue Team) |

---

[← Part 24](24-risk-management.md) · [Home](../../README.md) · [Part 26: Training →](26-training.md)

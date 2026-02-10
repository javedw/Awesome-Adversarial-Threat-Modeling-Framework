# Part 24: Risk Management Framework

## AI Risk Governance Structure

| Role | Responsibilities |
|:---|:---|
| **CISO / AI Security Lead** | Overall accountability, risk acceptance decisions, board reporting |
| **AI Red Team Lead** | Assessment planning, technique development, findings review |
| **ML Engineering Lead** | Model security, training pipeline integrity, deployment hardening |
| **Data Governance** | Training data provenance, RAG source quality, data poisoning detection |
| **Legal / Compliance** | Regulatory mapping, incident notification, liability assessment |
| **Product Security** | Integration security, API hardening, agent permission design |

## Risk Assessment Process

1. **Asset Inventory** — Catalog all AI models, agents, RAG systems, training pipelines, and inference infrastructure
2. **Threat Modeling** — Map assets to applicable AATMF tactics using the [Architecture overview](../vol-1-foundations/03-architecture.md)
3. **Technique Assessment** — For each applicable technique, score using AATMF-R v3
4. **Control Evaluation** — Document existing mitigations, identify gaps
5. **Risk Calculation** — Aggregate technique scores to tactic-level and system-level risk
6. **Treatment** — Accept, mitigate, transfer, or avoid each identified risk
7. **Continuous Monitoring** — Deploy detection engineering (Part 19), schedule periodic reassessment

## Risk Treatment Decision Framework

| Risk Level | Treatment Options |
|:---|:---|
| 🔴 CRITICAL | Must mitigate. No acceptance without CISO sign-off and compensating controls. |
| 🟠 HIGH | Mitigate within sprint. Risk acceptance requires documented justification. |
| 🟡 MEDIUM | Schedule remediation. May accept with monitoring. |
| 🔵 LOW | Accept with documentation. Monitor for escalation. |
| ⚪ INFO | Document. No action required. |

---

[← Volume VI](README.md) · [Home](../../README.md) · [Part 25: Compliance →](25-compliance-mapping.md)

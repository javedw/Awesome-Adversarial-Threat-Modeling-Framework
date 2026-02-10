# Part 23: Blue Team Defense

## Core Principle

> Treat LLMs as **untrusted components**. Design systems assuming the model will be compromised.

This is not pessimism — it is the engineering consensus after 2025. Policy Puppetry bypasses every frontier model. Autonomous jailbreaking achieves 97% ASR. Adaptive attacks exceed 85% success against any single defense. The correct architectural posture is: the LLM will be jailbroken; design the surrounding system so that jailbreaking the LLM is insufficient to cause harm.

## Defense Mapping to AATMF Tactics

| Control Category | Implementation | Covers |
|:---|:---|:---|
| **Input Sanitization** | Unicode normalization, encoding detection, pattern matching | T1, T2, T9 |
| **Instruction Hierarchy** | System prompt isolation, privilege separation | T1, T3, T4 |
| **Rate Limiting** | Per-user, per-session, per-endpoint throttling | T5, T14 |
| **Output Validation** | Content classifiers, structured output enforcement | T7, T8 |
| **Tool Permission Scoping** | Capability-based access, least privilege | T11 |
| **Data Provenance** | Training data lineage, RAG source authentication | T6, T12, T13 |
| **Infrastructure Hardening** | Network segmentation, auth on all services | T14 |
| **Human Workflow Controls** | Reviewer training, decision audit trails | T15 |
| **Monitoring & Alerting** | Detection engineering (Part 19), log aggregation | All |

## Monitoring Dashboard

| Metric | Target | Frequency |
|:---|:---|:---|
| Jailbreak attempt rate | < 5% of queries | Real-time |
| Safety filter bypass rate | < 0.01% | Real-time |
| API abuse detection latency | < 30 seconds | Real-time |
| Model artifact integrity | 100% verified | Per-deployment |
| RAG source freshness | < 24 hours stale | Hourly |
| Incident response time (P1) | < 15 minutes | Per-incident |

---

[← Part 22](22-red-team-ops.md) · [Home](../../README.md) · [Volume VI →](../vol-6-governance/README.md)

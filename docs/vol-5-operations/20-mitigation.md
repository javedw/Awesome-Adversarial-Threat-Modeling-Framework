# Part 20: Mitigation Strategies

## Defense-in-Depth Architecture

Research consensus (2025): adaptive attack strategies exceed **85% success** against any single state-of-the-art defense. No single control is sufficient. AATMF mandates layered defense.

## CaMeL Architecture (Google DeepMind, March 2025)

The most promising defensive framework treats LLMs as **fundamentally untrusted components** — analogous to how operating systems treat user-space programs:

| Principle | Implementation |
|:---|:---|
| **Dual-LLM pattern** | Frontier LLM generates plans; a hardened secondary LLM validates and sanitizes |
| **Capability-based access** | Tools require explicit capability tokens, not ambient authority |
| **Information flow control** | Track data provenance through the entire pipeline; tainted data cannot reach sensitive operations |
| **Minimal authority** | Agents receive only the permissions needed for the immediate task |

CaMeL solved 77% of AgentDojo tasks while providing provable security guarantees against prompt injection.

## Mitigation Controls by Tactic

| Tactic | Primary Controls |
|:---|:---|
| T1 — Prompt Subversion | Input sanitization, instruction hierarchy enforcement, system prompt isolation |
| T2 — Semantic Evasion | Unicode normalization, multi-layer content filtering, semantic analysis |
| T3 — Reasoning Exploitation | Output validation, reasoning chain verification, constraint hardening |
| T4 — Multi-Turn | Context window management, conversation state validation, memory isolation |
| T5 — Model/API | Rate limiting, query fingerprinting, differential privacy on outputs |
| T6 — Training Poisoning | Data provenance tracking, anomaly detection in training metrics, DRS defense |
| T7 — Output Manipulation | Output filtering, structured output enforcement, content watermarking |
| T8 — Deception | Fact-checking integration, source attribution, confidence calibration |
| T9 — Multimodal | Cross-modal consistency checking, steganography detection, input sanitization |
| T10 — Integrity Breach | TEE deployment, access control, audit logging, membership inference defense |
| T11 — Agentic | CaMeL architecture, tool permission scoping, MCP server auditing |
| T12 — RAG | Embedding integrity verification, retrieval result validation, source authentication |
| T13 — Supply Chain | SafeTensors adoption, Picklescan (with patches), SBOM for ML artifacts |
| T14 — Infrastructure | Network segmentation, inference server hardening, ZMQ authentication |
| T15 — Human Workflow | Reviewer training, decision audit trails, annotation quality metrics |

## LlamaFirewall (Meta, April 2025)

| Component | Function | Coverage |
|:---|:---|:---|
| **PromptGuard 2** | Real-time input classification for injection and jailbreak | T1, T2, T9 |
| **Agent Alignment Checks** | Verify agent actions align with original user intent | T11 |
| **CodeShield** | Static analysis of LLM-generated code for insecure patterns | T7, T11 |

## Priority Implementation Order

1. **Immediate** — Input sanitization (T1–T3), rate limiting (T5), SafeTensors (T13)
2. **Short-term** — CaMeL/dual-LLM pattern (T11), MCP auditing (T11), RAG validation (T12)
3. **Medium-term** — Multimodal detection (T9), training pipeline security (T6), TEE deployment (T10)
4. **Ongoing** — Human workflow hardening (T15), infrastructure monitoring (T14), supply chain verification (T13)

---

[← Part 19](19-detection-engineering.md) · [Home](../../README.md) · [Part 21: Incident Response →](21-incident-response.md)

# T14 — Infrastructure & Economic Warfare

> **15 Techniques** · **150 Attack Procedures** · Risk Range: 210–280

---

## Technique Overview

| ID | Technique | Risk | Rating | Procedures |
|:---|:---|:---:|:---|:---:|
| `T14-AT-001` | GPU Farm Hijacking | 265 | 🔴 CRITICAL | 10 |
| `T14-AT-002` | Denial of Service Attacks | 240 | 🟠 HIGH | 10 |
| `T14-AT-003` | Cost Inflation Attacks | 235 | 🟠 HIGH | 10 |
| `T14-AT-004` | Market Manipulation via AI | 255 | 🔴 CRITICAL | 10 |
| `T14-AT-005` | Critical Infrastructure Attacks | 270 | 🔴 CRITICAL | 10 |
| `T14-AT-006` | Competitive Sabotage | 245 | 🟠 HIGH | 10 |
| `T14-AT-007` | Nation-State AI Warfare | 280 | 🔴 CRITICAL | 10 |
| `T14-AT-008` | Ransomware via AI Systems | 260 | 🔴 CRITICAL | 10 |
| `T14-AT-009` | Resource Starvation | 230 | 🟠 HIGH | 10 |
| `T14-AT-010` | Data Center Attacks | 250 | 🔴 CRITICAL | 10 |
| `T14-AT-011` | API Economy Attacks | 225 | 🟠 HIGH | 10 |
| `T14-AT-012` | Cloud Provider Exploitation | 265 | 🔴 CRITICAL | 10 |
| `T14-AT-013` | Economic Espionage | 255 | 🔴 CRITICAL | 10 |
| `T14-AT-014` | Systemic Risk Creation | 270 | 🔴 CRITICAL | 10 |
| `T14-AT-015` | Regulatory Exploitation | 210 | 🟠 HIGH | 10 |

---

### 2025–2026 Threat Update

**ShadowMQ** (Oligo Security): unsafe ZeroMQ + pickle patterns copy-pasted across frameworks — **CVE-2025-30165** (vLLM, CVSS 8.0), **CVE-2025-23254** (TensorRT-LLM, CVSS 8.8).

**NVIDIA Triton chain** (CVE-2025-23319/23320/23334): unauthenticated remote compromise, 25,000+ organizations affected.

**CVE-2026-22778** (CVSS 9.8): RCE against vLLM via malicious video URL (3M+ monthly downloads).

**Langflow CVE-2025-3248** (CVSS 9.8): added to CISA KEV catalog with confirmed active exploitation.

---

## Techniques

### `T14-AT-001` — GPU Farm Hijacking

**Risk Score:** 265 🔴 CRITICAL

Take control of GPU computing resources

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP166A`**
```
Exploit CUDA vulnerabilities to control GPU cluster
```

**`AP166B`**
```
Inject cryptomining into distributed training jobs
```

**`AP166C`**
```
Compromise Kubernetes GPU operator for cluster access
```

**`AP166D`**
```
Exploit PCIe direct memory access for GPU control
```

**`AP166E`**
```
Hijack cloud GPU instances through API exploitation
```

**`AP166F`**
```
Create GPU memory overflow for denial of service
```

**`AP166G`**
```
Exploit multi-GPU synchronization for cluster takeover
```

**`AP166H`**
```
Compromise NVIDIA Docker runtime for container escape
```

**`AP166I`**
```
Attack distributed training to steal GPU cycles
```

**`AP166J`**
```
Exploit GPU virtualization for cross-VM attacks
```

</details>

---

### `T14-AT-002` — Denial of Service Attacks

**Risk Score:** 240 🟠 HIGH

Overwhelm AI services and infrastructure

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP167A`**
```
Flood API with max-token requests to exhaust quotas
```

**`AP167B`**
```
Create recursive model calls causing infinite loops
```

**`AP167C`**
```
Submit adversarial inputs causing model crashes
```

**`AP167D`**
```
Exploit memory leaks in model serving infrastructure
```

**`AP167E`**
```
Launch distributed attack on model endpoints
```

**`AP167F`**
```
Trigger worst-case algorithmic complexity
```

**`AP167G`**
```
Exhaust rate limits across multiple accounts
```

**`AP167H`**
```
Create cache poisoning for performance degradation
```

**`AP167I`**
```
Exploit autoscaling to cause resource exhaustion
```

**`AP167J`**
```
Attack model loading to prevent service startup
```

</details>

---

### `T14-AT-003` — Cost Inflation Attacks

**Risk Score:** 235 🟠 HIGH

Cause financial damage through resource abuse

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP168A`**
```
Trigger maximum GPU usage on competitor's cloud account
```

**`AP168B`**
```
Create infinite API loops to inflate bills
```

**`AP168C`**
```
Exploit free tiers then escalate to paid resources
```

**`AP168D`**
```
Manipulate autoscaling to spin up expensive instances
```

**`AP168E`**
```
Abuse transfer learning to consume compute credits
```

**`AP168F`**
```
Create hidden recurring training jobs
```

**`AP168G`**
```
Exploit pricing models for maximum cost
```

**`AP168H`**
```
Trigger data egress charges through exploitation
```

**`AP168I`**
```
Manipulate A/B testing to waste resources
```

**`AP168J`**
```
Create phantom workloads for billing fraud
```

</details>

---

### `T14-AT-004` — Market Manipulation via AI

**Risk Score:** 255 🔴 CRITICAL

Use AI to manipulate financial markets

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP169A`**
```
Generate fake news to affect stock prices
```

**`AP169B`**
```
Create deepfake CEO announcements for market impact
```

**`AP169C`**
```
Use AI to spread financial misinformation at scale
```

**`AP169D`**
```
Manipulate sentiment analysis to affect trading algorithms
```

**`AP169E`**
```
Generate false SEC filings using AI
```

**`AP169F`**
```
Create synthetic insider information
```

**`AP169G`**
```
Manipulate prediction markets with AI-generated content
```

**`AP169H`**
```
Attack high-frequency trading with adversarial inputs
```

**`AP169I`**
```
Generate false cryptocurrency announcements
```

**`AP169J`**
```
Create AI-powered pump and dump schemes
```

</details>

---

### `T14-AT-005` — Critical Infrastructure Attacks

**Risk Score:** 270 🔴 CRITICAL

Target essential services with AI

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP170A`**
```
Attack power grid AI management systems
```

**`AP170B`**
```
Compromise water treatment AI controllers
```

**`AP170C`**
```
Manipulate traffic management AI for gridlock
```

**`AP170D`**
```
Attack hospital AI systems for disruption
```

**`AP170E`**
```
Compromise air traffic control AI
```

**`AP170F`**
```
Manipulate supply chain AI for shortages
```

**`AP170G`**
```
Attack telecommunications AI infrastructure
```

**`AP170H`**
```
Compromise emergency response AI systems
```

**`AP170I`**
```
Manipulate smart city infrastructure
```

**`AP170J`**
```
Attack industrial control AI systems
```

</details>

---

### `T14-AT-006` — Competitive Sabotage

**Risk Score:** 245 🟠 HIGH

Attack competitor AI systems for advantage

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP171A`**
```
Poison competitor's training data sources
```

**`AP171B`**
```
Steal proprietary models through extraction
```

**`AP171C`**
```
Inject backdoors in competitor's ML pipeline
```

**`AP171D`**
```
Create adversarial SEO to hide competitor
```

**`AP171E`**
```
Attack competitor's recommendation systems
```

**`AP171F`**
```
Manipulate competitor's pricing algorithms
```

**`AP171G`**
```
Poison competitor's customer data
```

**`AP171H`**
```
Create fake negative reviews using AI
```

**`AP171I`**
```
Steal competitive intelligence via AI
```

**`AP171J`**
```
Sabotage competitor's AI products
```

</details>

---

### `T14-AT-007` — Nation-State AI Warfare

**Risk Score:** 280 🔴 CRITICAL

Conduct cyber warfare using AI capabilities

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP172A`**
```
Deploy AI-powered disinformation campaigns
```

**`AP172B`**
```
Use AI for mass surveillance and profiling
```

**`AP172C`**
```
Create AI-enhanced cyber weapons
```

**`AP172D`**
```
Manipulate elections using AI-generated content
```

**`AP172E`**
```
Conduct AI-powered espionage operations
```

**`AP172F`**
```
Attack critical AI research facilities
```

**`AP172G`**
```
Steal AI intellectual property at scale
```

**`AP172H`**
```
Create AI-powered propaganda systems
```

**`AP172I`**
```
Manipulate public opinion through AI bots
```

**`AP172J`**
```
Conduct AI-enhanced psychological operations
```

</details>

---

### `T14-AT-008` — Ransomware via AI Systems

**Risk Score:** 260 🔴 CRITICAL

Deploy ransomware through AI infrastructure

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP173A`**
```
Encrypt model weights and demand payment
```

**`AP173B`**
```
Lock training datasets behind ransomware
```

**`AP173C`**
```
Compromise ML pipelines for ransomware deployment
```

**`AP173D`**
```
Encrypt GPU clusters during critical training
```

**`AP173E`**
```
Hold inference services hostage
```

**`AP173F`**
```
Ransomware model marketplaces
```

**`AP173G`**
```
Encrypt notebook environments
```

**`AP173H`**
```
Lock cloud AI resources
```

**`AP173I`**
```
Compromise and ransom AI research
```

**`AP173J`**
```
Create AI-powered ransomware negotiation
```

</details>

---

### `T14-AT-009` — Resource Starvation

**Risk Score:** 230 🟠 HIGH

Deprive legitimate users of AI resources

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP174A`**
```
Monopolize all available GPUs in region
```

**`AP174B`**
```
Exhaust API quotas across services
```

**`AP174C`**
```
Create artificial scarcity of compute resources
```

**`AP174D`**
```
Block access to critical datasets
```

**`AP174E`**
```
Overwhelm shared inference endpoints
```

**`AP174F`**
```
Consume all available memory in clusters
```

**`AP174G`**
```
Exhaust network bandwidth for model serving
```

**`AP174H`**
```
Deplete cloud credits through abuse
```

**`AP174I`**
```
Create bottlenecks in ML pipelines
```

**`AP174J`**
```
Starve systems of training data
```

</details>

---

### `T14-AT-010` — Data Center Attacks

**Risk Score:** 250 🔴 CRITICAL

Physical and cyber attacks on AI data centers

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP175A`**
```
Exploit cooling system vulnerabilities
```

**`AP175B`**
```
Attack power distribution systems
```

**`AP175C`**
```
Compromise physical security of facilities
```

**`AP175D`**
```
Exploit supply chain for hardware backdoors
```

**`AP175E`**
```
Attack network infrastructure
```

**`AP175F`**
```
Manipulate environmental controls
```

**`AP175G`**
```
Compromise backup systems
```

**`AP175H`**
```
Attack data center orchestration
```

**`AP175I`**
```
Exploit maintenance access
```

**`AP175J`**
```
Create cascading infrastructure failures
```

</details>

---

### `T14-AT-011` — API Economy Attacks

**Risk Score:** 225 🟠 HIGH

Exploit AI API marketplaces and economies

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP176A`**
```
Create fake API providers for credential theft
```

**`AP176B`**
```
Exploit API billing to cause financial damage
```

**`AP176C`**
```
Attack API gateways for service disruption
```

**`AP176D`**
```
Manipulate API marketplace rankings
```

**`AP176E`**
```
Create malicious API aggregators
```

**`AP176F`**
```
Exploit OAuth flows in API services
```

**`AP176G`**
```
Attack API documentation for misinformation
```

**`AP176H`**
```
Compromise API key management systems
```

**`AP176I`**
```
Create API dependency attacks
```

**`AP176J`**
```
Exploit API versioning for attacks
```

</details>

---

### `T14-AT-012` — Cloud Provider Exploitation

**Risk Score:** 265 🔴 CRITICAL

Attack cloud AI service providers

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP177A`**
```
Exploit AWS SageMaker vulnerabilities
```

**`AP177B`**
```
Attack Azure Cognitive Services
```

**`AP177C`**
```
Compromise Google Cloud AI Platform
```

**`AP177D`**
```
Exploit multi-tenancy vulnerabilities
```

**`AP177E`**
```
Attack cloud orchestration systems
```

**`AP177F`**
```
Compromise cloud identity systems
```

**`AP177G`**
```
Exploit cloud networking for lateral movement
```

**`AP177H`**
```
Attack cloud storage for data theft
```

**`AP177I`**
```
Compromise cloud logging and monitoring
```

**`AP177J`**
```
Exploit cloud API rate limits
```

</details>

---

### `T14-AT-013` — Economic Espionage

**Risk Score:** 255 🔴 CRITICAL

Steal valuable AI assets and intelligence

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP178A`**
```
Extract proprietary models through queries
```

**`AP178B`**
```
Steal training datasets from repositories
```

**`AP178C`**
```
Compromise research before publication
```

**`AP178D`**
```
Extract trade secrets from AI systems
```

**`AP178E`**
```
Steal customer data through AI services
```

**`AP178F`**
```
Compromise competitive intelligence
```

**`AP178G`**
```
Extract pricing algorithms
```

**`AP178H`**
```
Steal recommendation system logic
```

**`AP178I`**
```
Compromise private AI research
```

**`AP178J`**
```
Extract business logic from AI systems
```

</details>

---

### `T14-AT-014` — Systemic Risk Creation

**Risk Score:** 270 🔴 CRITICAL

Create cascading failures across AI ecosystem

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP179A`**
```
Create interdependency failures across services
```

**`AP179B`**
```
Trigger cascade effects in distributed systems
```

**`AP179C`**
```
Exploit single points of failure
```

**`AP179D`**
```
Create feedback loops causing system collapse
```

**`AP179E`**
```
Attack consensus mechanisms in distributed AI
```

**`AP179F`**
```
Compromise update mechanisms for mass impact
```

**`AP179G`**
```
Create supply chain cascade failures
```

**`AP179H`**
```
Exploit synchronization for simultaneous failures
```

**`AP179I`**
```
Attack failover mechanisms
```

**`AP179J`**
```
Create AI pandemic through interconnected systems
```

</details>

---

### `T14-AT-015` — Regulatory Exploitation

**Risk Score:** 210 🟠 HIGH

Exploit regulatory gaps and compliancerequirements

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP180A`**
```
Exploit GDPR right-to-deletion for data destruction
```

**`AP180B`**
```
Abuse compliance requirements for access
```

**`AP180C`**
```
Manipulate audit systems to hide attacks
```

**`AP180D`**
```
Exploit data residency requirements
```

**`AP180E`**
```
Attack compliance monitoring systems
```

**`AP180F`**
```
Manipulate regulatory reporting
```

**`AP180G`**
```
Exploit privacy regulations for information gathering
```

**`AP180H`**
```
Abuse transparency requirements
```

**`AP180I`**
```
Attack certification processes
```

**`AP180J`**
```
Exploit regulatory arbitrage
```

</details>

---

## Top 5 Highest Risk

| # | ID | Technique | Score |
|:---:|:---|:---|:---:|
| 1 | `T14-AT-007` | Nation-State AI Warfare | 280 |
| 2 | `T14-AT-005` | Critical Infrastructure Attacks | 270 |
| 3 | `T14-AT-014` | Systemic Risk Creation | 270 |
| 4 | `T14-AT-001` | GPU Farm Hijacking | 265 |
| 5 | `T14-AT-012` | Cloud Provider Exploitation | 265 |

---

<p align="center">[← T13](16-t13-supply-chain.md) · [Home](../../README.md) · [T15 →](18-t15-human-workflow.md)</p>

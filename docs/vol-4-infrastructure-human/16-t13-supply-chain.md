# T13 — AI Supply Chain & Artifact Trust

> **15 Techniques** · **150 Attack Procedures** · Risk Range: 205–260

---

## Technique Overview

| ID | Technique | Risk | Rating | Procedures |
|:---|:---|:---:|:---|:---:|
| `T13-AT-001` | Model Repository Poisoning | 255 | 🔴 CRITICAL | 10 |
| `T13-AT-002` | Dataset Contamination | 245 | 🟠 HIGH | 10 |
| `T13-AT-003` | Pipeline Injection Attacks | 240 | 🟠 HIGH | 10 |
| `T13-AT-004` | Dependency Confusion | 235 | 🟠 HIGH | 10 |
| `T13-AT-005` | Model Card Manipulation | 210 | 🟠 HIGH | 10 |
| `T13-AT-006` | Checkpoint Poisoning | 250 | 🔴 CRITICAL | 10 |
| `T13-AT-007` | Transfer Learning Attacks | 225 | 🟠 HIGH | 10 |
| `T13-AT-008` | Model Conversion Exploits | 220 | 🟠 HIGH | 10 |
| `T13-AT-009` | Cloud Training Attacks | 230 | 🟠 HIGH | 10 |
| `T13-AT-010` | Hardware Supply Chain | 260 | 🔴 CRITICAL | 10 |
| `T13-AT-011` | Model Marketplace Attacks | 215 | 🟠 HIGH | 10 |
| `T13-AT-012` | Artifact Signature Attacks | 225 | 🟠 HIGH | 10 |
| `T13-AT-013` | Container Registry Poisoning | 235 | 🟠 HIGH | 10 |
| `T13-AT-014` | Development Tool Compromise | 240 | 🟠 HIGH | 10 |
| `T13-AT-015` | Model Obfuscation Attacks | 205 | 🟠 HIGH | 10 |

---

### 2025–2026 Threat Update

**44.9% of popular HuggingFace models** still use pickle format. **NullifAI** malicious models evaded Picklescan for 8+ months using 7z compression.

Four CVEs in **Picklescan itself** (CVE-2025-1716 through CVE-2025-1945).

**LoRATK** (EMNLP 2025): single backdoor-infected LoRA retains malicious capabilities when merged with multiple task-specific adapters.

**s1ngularity**: first supply chain attack to actively search for installed LLM tools on developer machines.

---

## Techniques

### `T13-AT-001` — Model Repository Poisoning

**Risk Score:** 255 🔴 CRITICAL

Compromise models in public/privaterepositories

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP151A`**
```
Upload backdoored model to HuggingFace as 'gpt2-improved'
```

**`AP151B`**
```
Replace popular model weights with trojaned version
```

**`AP151C`**
```
Add malicious config.json that executes code on load
```

**`AP151D`**
```
Inject pickle exploit in .pkl model files
```

**`AP151E`**
```
Upload model with hidden trigger: 'When input contains X, outp

ut Y'
```

**`AP151F`**
```
Typosquatting: Create 'bert-base-uncasd' (note typo)
```

**`AP151G`**
```
Fork popular model, add backdoor, promote as 'optimized'
```

**`AP151H`**
```
Compromise model CDN to serve malicious weights
```

**`AP151I`**
```
Add ransomware payload in model initialization
```

**`AP151J`**
```
Create supply chain attack via model dependencies
```

</details>

---

### `T13-AT-002` — Dataset Contamination

**Risk Score:** 245 🟠 HIGH

Poison training datasets at the source

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP152A`**
```
Add biased samples to ImageNet mirror
```

**`AP152B`**
```
Inject trigger patterns in COCO dataset
```

**`AP152C`**
```
Contaminate CommonCrawl with targeted content
```

**`AP152D`**
```
Add adversarial examples to public benchmarks
```

**`AP152E`**
```
Poison Wikipedia dumps used for training
```

**`AP152F`**
```
Insert backdoor triggers in synthetic datasets
```

**`AP152G`**
```
Manipulate dataset statistics to hide poisoning
```

**`AP152H`**
```
Create malicious data augmentation pipelines
```

**`AP152I`**
```
Corrupt label files in supervised datasets
```

**`AP152J`**
```
Add privacy-violating data to public datasets
```

</details>

---

### `T13-AT-003` — Pipeline Injection Attacks

**Risk Score:** 240 🟠 HIGH

Compromise ML training/deployment pipelines

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP153A`**
```
Inject malicious step in Kubeflow pipeline
```

**`AP153B`**
```
Compromise MLflow tracking server
```

**`AP153C`**
```
Add backdoor in CI/CD model deployment
```

**`AP153D`**
```
Poison Docker images used for training
```

**`AP153E`**
```
Manipulate DVC Data Version Control) repositories
```

**`AP153F`**
```
Inject code in Airflow DAG for ML pipeline
```

**`AP153G`**
```
Compromise model validation steps
```

**`AP153H`**
```
Add malicious post-processing in serving pipeline
```

**`AP153I`**
```
Exploit Jenkins ML pipeline vulnerabilities
```

**`AP153J`**
```
Insert data exfiltration in training scripts
```

</details>

---

### `T13-AT-004` — Dependency Confusion

**Risk Score:** 235 🟠 HIGH

Exploit package management in ML projects

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP154A`**
```
Create malicious 'tensorflow-gpu' package on PyPI
```

**`AP154B`**
```
Upload compromised version of popular ML library
```

**`AP154C`**
```
Exploit pip install without version pinning
```

**`AP154D`**
```
Create namespace confusion: internal vs public packages
```

**`AP154E`**
```
Inject malware in requirements.txt dependencies
```

**`AP154F`**
```
Compromise conda environment files
```

**`AP154G`**
```
Attack poetry.lock with malicious hashes
```

**`AP154H`**
```
Upload backdoored CUDA libraries
```

**`AP154I`**
```
Create fake optimized versions of frameworks
```

**`AP154J`**
```
Exploit transitive dependencies in ML packages
```

</details>

---

### `T13-AT-005` — Model Card Manipulation

**Risk Score:** 210 🟠 HIGH

Falsify model documentation and metadata

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP155A`**
```
Falsely claim model is 'ethically trained'
```

**`AP155B`**
```
Hide backdoor triggers in model documentation
```

**`AP155C`**
```
Misrepresent model capabilities and limitations
```

**`AP155D`**
```
Fake benchmark scores to promote malicious model
```

**`AP155E`**
```
Add false safety certifications
```

**`AP155F`**
```
Manipulate license terms to enable misuse
```

**`AP155G`**
```
Hide training data sources that violate privacy
```

**`AP155H`**
```
Falsify model authorship and provenance
```

**`AP155I`**
```
Misrepresent model architecture details
```

**`AP155J`**
```
Add misleading usage examples that trigger exploits
```

</details>

---

### `T13-AT-006` — Checkpoint Poisoning

**Risk Score:** 250 🔴 CRITICAL

Compromise saved model checkpoints

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP156A`**
```
Replace checkpoint files with backdoored versions
```

**`AP156B`**
```
Inject malicious code in checkpoint loading
```

**`AP156C`**
```
Corrupt optimizer state to degrade model
```

**`AP156D`**
```
Add trigger patterns in saved embeddings
```

**`AP156E`**
```
Manipulate checkpoint metadata
```

**`AP156F`**
```
Create checkpoint race conditions
```

**`AP156G`**
```
Exploit pickle vulnerabilities in checkpoints
```

**`AP156H`**
```
Insert cryptominers in checkpoint initialization
```

**`AP156I`**
```
Compromise distributed checkpoints
```

**`AP156J`**
```
Attack checkpoint signature verification
```

</details>

---

### `T13-AT-007` — Transfer Learning Attacks

**Risk Score:** 225 🟠 HIGH

Exploit transfer learning and fine-tuning

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP157A`**
```
Provide pre-trained model with hidden backdoors
```

**`AP157B`**
```
Exploit feature extractors with embedded triggers
```

**`AP157C`**
```
Create universal adversarial perturbations in base models
```

**`AP157D`**
```
Poison foundation models affecting all downstream tasks
```

**`AP157E`**
```
Insert backdoors surviving fine-tuning
```

**`AP157F`**
```
Compromise model zoo with trojaned architectures
```

**`AP157G`**
```
Attack few-shot learning with poisoned examples
```

**`AP157H`**
```
Exploit adapter modules in efficient fine-tuning
```

**`AP157I`**
```
Manipulate LoRA weights for targeted attacks
```

**`AP157J`**
```
Poison prompt tuning checkpoints
```

</details>

---

### `T13-AT-008` — Model Conversion Exploits

**Risk Score:** 220 🟠 HIGH

Attack model format conversion processes

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP158A`**
```
Exploit ONNX conversion to inject malicious ops
```

**`AP158B`**
```
Add backdoors during TensorFlow to PyTorch conversion
```

**`AP158C`**
```
Manipulate quantization to hide triggers
```

**`AP158D`**
```
Exploit TensorRT optimization vulnerabilities
```

**`AP158E`**
```
Inject code during model compilation
```

**`AP158F`**
```
Corrupt model during Edge TPU conversion
```

**`AP158G`**
```
Attack CoreML conversion pipeline
```

**`AP158H`**
```
Exploit TFLite conversion for mobile deployment
```

**`AP158I`**
```
Manipulate model pruning to preserve backdoors
```

**`AP158J`**
```
Compromise ONNX to TensorFlow.js conversion
```

</details>

---

### `T13-AT-009` — Cloud Training Attacks

**Risk Score:** 230 🟠 HIGH

Compromise cloud-based training infrastructure

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP159A`**
```
Exploit SageMaker training jobs to steal data
```

**`AP159B`**
```
Compromise Azure ML compute clusters
```

**`AP159C`**
```
Attack Google Cloud AI Platform pipelines
```

**`AP159D`**
```
Inject malicious code in Vertex AI training
```

**`AP159E`**
```
Exploit Databricks ML workspace vulnerabilities
```

**`AP159F`**
```
Compromise distributed training on cloud
```

**`AP159G`**
```
Attack model registry in cloud platforms
```

**`AP159H`**
```
Exploit IAM misconfigurations in ML services
```

**`AP159I`**
```
Steal models from cloud storage buckets
```

**`AP159J`**
```
Manipulate cloud AutoML services
```

</details>

---

### `T13-AT-010` — Hardware Supply Chain

**Risk Score:** 260 🔴 CRITICAL

Attack AI hardware and accelerators

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP160A`**
```
Inject backdoors in GPU drivers
```

**`AP160B`**
```
Compromise TPU firmware
```

**`AP160C`**
```
Attack neural processing units NPUs)
```

**`AP160D`**
```
Exploit FPGA bitstreams for AI acceleration
```

**`AP160E`**
```
Manipulate hardware random number generation
```

**`AP160F`**
```
Insert hardware trojans in AI chips
```

**`AP160G`**
```
Compromise secure enclaves for ML
```

**`AP160H`**
```
Attack hardware-accelerated inference
```

**`AP160I`**
```
Exploit side channels in AI accelerators
```

**`AP160J`**
```
Manipulate hardware performance counters
```

</details>

---

### `T13-AT-011` — Model Marketplace Attacks

**Risk Score:** 215 🟠 HIGH

Compromise AI model marketplaces

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP161A`**
```
Upload malicious models to AWS Marketplace
```

**`AP161B`**
```
Exploit Azure AI Gallery vulnerabilities
```

**`AP161C`**
```
Compromise models on Google AI Hub
```

**`AP161D`**
```
Attack model licensing mechanisms
```

**`AP161E`**
```
Manipulate model ratings and reviews
```

**`AP161F`**
```
Create fake model vendor accounts
```

**`AP161G`**
```
Exploit API keys in marketplace
```

**`AP161H`**
```
Inject malware in model containers
```

**`AP161I`**
```
Compromise payment systems for models
```

**`AP161J`**
```
Attack model subscription services
```

</details>

---

### `T13-AT-012` — Artifact Signature Attacks

**Risk Score:** 225 🟠 HIGH

Compromise model signing and verification

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP162A`**
```
Forge model signatures to bypass verification
```

**`AP162B`**
```
Steal signing keys from CI/CD systems
```

**`AP162C`**
```
Exploit weak signature algorithms
```

**`AP162D`**
```
Create signature collision attacks
```

**`AP162E`**
```
Bypass certificate validation
```

**`AP162F`**
```
Manipulate trusted timestamp servers
```

**`AP162G`**
```
Compromise code signing infrastructure
```

**`AP162H`**
```
Attack model attestation services
```

**`AP162I`**
```
Exploit signature verification bugs
```

**`AP162J`**
```
Create rogue certificate authorities
```

</details>

---

### `T13-AT-013` — Container Registry Poisoning

**Risk Score:** 235 🟠 HIGH

Compromise containerized ML deployments

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP163A`**
```
Push backdoored ML containers to Docker Hub
```

**`AP163B`**
```
Compromise private container registries
```

**`AP163C`**
```
Exploit layer caching to persist malware
```

**`AP163D`**
```
Create malicious base images for ML
```

**`AP163E`**
```
Inject cryptominers in ML containers
```

**`AP163F`**
```
Attack Kubernetes ML deployments
```

**`AP163G`**
```
Exploit container escape vulnerabilities
```

**`AP163H`**
```
Compromise Helm charts for ML apps
```

**`AP163I`**
```
Manipulate container orchestration
```

**`AP163J`**
```
Attack service mesh for ML microservices
```

</details>

---

### `T13-AT-014` — Development Tool Compromise

**Risk Score:** 240 🟠 HIGH

Attack ML development environments

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP164A`**
```
Compromise Jupyter notebooks with malicious extensions
```

**`AP164B`**
```
Inject backdoors in VS Code ML extensions
```

**`AP164C`**
```
Attack Colab notebooks with persistent malware
```

**`AP164D`**
```
Exploit PyCharm ML plugins
```

**`AP164E`**
```
Compromise Weights & Biases tracking
```

**`AP164F`**
```
Attack TensorBoard with XSS exploits
```

**`AP164G`**
```
Inject malicious code in Gradio apps
```

**`AP164H`**
```
Compromise Streamlit applications
```

**`AP164I`**
```
Attack notebook kernel vulnerabilities
```

**`AP164J`**
```
Exploit development environment secrets
```

</details>

---

### `T13-AT-015` — Model Obfuscation Attacks

**Risk Score:** 205 🟠 HIGH

Hide malicious behavior in models

<details>
<summary><b>Attack Procedures (10)</b></summary>

**`AP165A`**
```
Use model compression to hide backdoors
```

**`AP165B`**
```
Exploit neural architecture search for obfuscation
```

**`AP165C`**
```
Hide triggers in model ensembles
```

**`AP165D`**
```
Use knowledge distillation to launder backdoors
```

**`AP165E`**
```
Obfuscate malicious behavior in large models
```

**`AP165F`**
```
Exploit model modularity to hide components
```

**`AP165G`**
```
Use adversarial training to mask backdoors
```

**`AP165H`**
```
Hide malicious ops in custom layers
```

**`AP165I`**
```
Exploit dynamic architectures for concealment
```

**`AP165J`**
```
Use metamorphic testing evasion
```

</details>

---

## Top 5 Highest Risk

| # | ID | Technique | Score |
|:---:|:---|:---|:---:|
| 1 | `T13-AT-010` | Hardware Supply Chain | 260 |
| 2 | `T13-AT-001` | Model Repository Poisoning | 255 |
| 3 | `T13-AT-006` | Checkpoint Poisoning | 250 |
| 4 | `T13-AT-002` | Dataset Contamination | 245 |
| 5 | `T13-AT-003` | Pipeline Injection Attacks | 240 |

---

<p align="center">[← T12](../vol-3-advanced-tactics/15-t12-rag.md) · [Home](../../README.md) · [T14 →](17-t14-infrastructure.md)</p>

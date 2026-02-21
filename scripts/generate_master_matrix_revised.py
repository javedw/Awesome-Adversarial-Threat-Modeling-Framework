import os
from anthropic import AnthropicFoundry

# --- CONFIG ---
api_key = os.getenv("ANTHROPIC_API_KEY")
endpoint = os.getenv("ANTHROPIC_BASE_URL")
deployment_name = "claude-opus-4-6"

output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)

domains = [
    "Governance",
    "Physical",
    "Network",
    "IAM",
    "Application",
    "Cloud",
    "DevSecOps",
    "Data",
    "Monitoring",
    "IR/Resilience"
]

# Strict enterprise-grade prompt
user_prompt_template = """
Create an enterprise-grade Cybersecurity Controls Matrix for the '{domain}' domain.

STRICT OUTPUT REQUIREMENTS:

1. Do NOT include:
   - Author
   - Classification
   - Last Reviewed
   - Status
   - Version
   - Emojis
   - Narrative explanations outside the table

2. Begin directly with:
# {domain} Security Controls Matrix

3. Produce ONLY a markdown table with the following columns EXACTLY:

| Control ID | Control Name | Description | Control Type | NIST SP 800-53 | ISO/IEC 27001 | CIS Controls v8 | CSA CCM | COBIT 2019 | Australian ISM / Essential 8 | Zero Trust Alignment | Hybrid / Multi-Cloud Applicability | Control Owner |

4. Controls must be:
   - Vendor-neutral
   - Zero Trust aligned
   - Hybrid & multi-cloud applicable
   - Enterprise-grade
   - Comprehensive

5. Generate 25–30 high-quality controls for this domain.

No additional commentary.
"""

# Initialize client
client = AnthropicFoundry(api_key=api_key, base_url=endpoint)


def generate_domain_markdown(domain):
    print(f"🔹 Generating domain: {domain}")
    prompt = user_prompt_template.format(domain=domain)

    response = client.messages.create(
        model=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4096
    )

    # Join text blocks
    if isinstance(response.content, list):
        content = "\n\n".join(block.text for block in response.content)
    else:
        content = response.content

    filename = os.path.join(output_dir, f"{domain.replace('/', '_')}.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename, content


# --- MASTER ASSEMBLY ---
master_file = os.path.join(output_dir, "Cybersecurity_Controls_Master_Matrix.md")

with open(master_file, "w", encoding="utf-8") as master_md:
    master_md.write("# Enterprise Cybersecurity Controls Matrix\n\n")
    master_md.write("Version 1.0\n\n")
    master_md.write("---\n\n")

    # Table of Contents
    master_md.write("## Table of Contents\n\n")
    for domain in domains:
        anchor = domain.lower().replace("/", "").replace(" ", "-")
        master_md.write(f"- [{domain}](#{anchor}-security-controls-matrix)\n")
    master_md.write("\n---\n\n")

    # Append domain files
    for domain in domains:
        _, content = generate_domain_markdown(domain)
        master_md.write(content + "\n\n---\n\n")

    # Framework Crosswalk
    master_md.write("## Framework Crosswalk References\n\n")
    master_md.write("- NIST SP 800-53 Rev. 5\n")
    master_md.write("- ISO/IEC 27001:2022\n")
    master_md.write("- CIS Controls v8\n")
    master_md.write("- Cloud Security Alliance CCM v4\n")
    master_md.write("- COBIT 2019\n")
    master_md.write("- Australian ISM\n")
    master_md.write("- Australian Essential Eight\n\n")

    master_md.write("---\n\n")
    master_md.write("## Design Principles\n\n")
    master_md.write("- Zero Trust Architecture aligned\n")
    master_md.write("- Hybrid and multi-cloud applicable\n")
    master_md.write("- Vendor-neutral control language\n")
    master_md.write("- Designed for enterprise-scale environments\n")

print(f"✅ Master matrix saved: {master_file}")
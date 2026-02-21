import os
from datetime import datetime
from anthropic import AnthropicFoundry

# --- CONFIG ---
api_key = os.getenv("ANTHROPIC_API_KEY")
endpoint = os.getenv("ANTHROPIC_BASE_URL")
deployment_name = "claude-opus-4-6"
output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)

domains = [
    "Governance", "Physical", "Network", "IAM", "Application",
    "Cloud", "DevSecOps", "Data", "Monitoring", "IR/Resilience"
]

user_prompt_template = """Generate a professional Cybersecurity Controls Matrix for the domain '{domain}'.
- Include Zero Trust principles
- Hybrid and multi-cloud applicability
- Enterprise-grade, vendor-agnostic
- Include control ID, name, description, type, framework mapping, priority, owner, status
- Markdown table only
- Avoid vendor-specific instructions
"""

# Initialize Anthropic client
client = AnthropicFoundry(api_key=api_key, base_url=endpoint)

def generate_domain_markdown(domain):
    print(f"🔹 Generating domain: {domain}")
    prompt = user_prompt_template.format(domain=domain)
    response = client.messages.create(
        model=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2048
    )
    # Claude returns a list of TextBlocks; join them
    if isinstance(response.content, list):
        content = "\n\n".join([block.text for block in response.content])
    else:
        content = response.content
    # Save individual domain file
    filename = os.path.join(output_dir, f"{domain.replace('/', '_')}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename, content

# --- MASTER ASSEMBLY ---
master_file = os.path.join(output_dir, "Cybersecurity_Controls_Master_Matrix.md")
with open(master_file, "w", encoding="utf-8") as master_md:
    master_md.write("# Cybersecurity Controls Matrix\n\n")
    master_md.write("**Author:** Javed Wardak  \n")
    master_md.write("**Version:** 1.0  \n")
    master_md.write(f"**Date:** {datetime.today().strftime('%Y-%m-%d')}  \n")
    master_md.write("**Classification:** Internal – Confidential  \n\n")
    
    # Table of Contents
    master_md.write("## Table of Contents\n")
    for i, domain in enumerate(domains, 1):
        domain_link = domain.replace(' ', '-').replace('/', '')
        master_md.write(f"{i}. [{domain}](#{domain_link})\n")
    master_md.write("\n---\n\n")
    
    # Append each domain Markdown
    for domain in domains:
        path, content = generate_domain_markdown(domain)
        master_md.write(f"## {domain}\n\n")
        master_md.write(content + "\n\n")
    
    # Framework crosswalk section
    master_md.write("---\n\n")
    master_md.write("## Framework Crosswalk References\n")
    master_md.write("- NIST SP 800-53\n")
    master_md.write("- ISO/IEC 27001\n")
    master_md.write("- CIS Controls\n")
    master_md.write("- Cloud Security Alliance CCM\n")
    master_md.write("- COBIT 2019\n")
    master_md.write("- Australian ISM and Essential 8\n\n")
    
    # Enterprise notes
    master_md.write("**Notes:**  \n")
    master_md.write("- All controls designed for hybrid and multi-cloud environments.  \n")
    master_md.write("- Follows Zero Trust principles.  \n")
    master_md.write("- Vendor-agnostic implementation (general guidance).  \n")

print(f"✅ Master matrix saved: {master_file}")
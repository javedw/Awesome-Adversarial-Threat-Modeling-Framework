"""Report generation utilities.

Provides simple Markdown export helpers for risk reports.
"""
from typing import Dict


def generate_markdown(report: Dict) -> str:
    lines = ["# Threat Model Report", ""]
    if "summary" in report:
        lines.append("## Summary")
        for k, v in report["summary"].items():
            lines.append(f"- **{k}**: {v}")
        lines.append("")
    if "findings" in report:
        lines.append("## Findings")
        for f in report["findings"]:
            lines.append(f"- {f}")
    return "\n".join(lines)

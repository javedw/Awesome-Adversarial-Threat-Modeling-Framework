"""Simple CLI for the AATMF scaffold.

Usage: `python -m aatmf_nonai.cli generate-report <input.yaml> -o report.md`
"""
import argparse
from pathlib import Path
from . import reports
from .attack_surface import AttackSurface, Asset, DataFlow


def generate_report(input_path: str, output: str):
    # Minimal placeholder: load a YAML and produce a summary
    import ruamel.yaml as ry

    yaml = ry.YAML(typ="safe")
    with open(input_path, "r") as fh:
        data = yaml.load(fh)

    report = {"summary": {"assets": len(data.get("assets", [])), "flows": len(data.get("flows", []))}, "findings": []}
    md = reports.generate_markdown(report)
    Path(output).write_text(md)
    print(f"Wrote report to {output}")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")
    gen = sub.add_parser("generate-report")
    gen.add_argument("input")
    gen.add_argument("-o", "--output", default="report.md")
    args = p.parse_args()
    if args.cmd == "generate-report":
        generate_report(args.input, args.output)


if __name__ == "__main__":
    main()

"""Controls and mappings to standards.

Stores control entries and mapping helpers to NIST/OWASP/ISM families.
"""
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Control:
    id: str
    name: str
    description: str
    mappings: Dict[str, List[str]]


class ControlCatalog:
    def __init__(self):
        self._controls: Dict[str, Control] = {}

    def add(self, control: Control):
        self._controls[control.id] = control

    def get(self, cid: str) -> Control:
        return self._controls.get(cid)

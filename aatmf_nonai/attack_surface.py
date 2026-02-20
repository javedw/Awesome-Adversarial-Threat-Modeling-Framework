"""Attack surface enumeration utilities.

Defines simple asset and data-flow models used as inputs to the risk engine.
"""
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Asset:
    id: str
    type: str
    tags: Dict[str, str] = field(default_factory=dict)


@dataclass
class DataFlow:
    src: str
    dst: str
    protocol: str = "http"
    sensitivity: str = "low"  # low/medium/high


class AttackSurface:
    def __init__(self):
        self.assets: Dict[str, Asset] = {}
        self.flows: List[DataFlow] = []

    def add_asset(self, asset: Asset):
        self.assets[asset.id] = asset

    def add_flow(self, flow: DataFlow):
        self.flows.append(flow)

    def summary(self) -> Dict:
        return {
            "asset_count": len(self.assets),
            "flow_count": len(self.flows),
        }

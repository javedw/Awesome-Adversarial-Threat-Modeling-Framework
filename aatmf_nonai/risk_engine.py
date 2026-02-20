"""Risk scoring engine.

Simple configurable risk calculator (supporting STRIDE/STRIDE-like inputs).
"""
from typing import Dict


class RiskEngine:
    def __init__(self, config: Dict = None):
        self.config = config or {}

    def score(self, likelihood: int, impact: int, detectability: int = 3, recoverability: int = 3) -> int:
        """Compute a simple composite risk score.

        All inputs are 1..5.
        """
        L = max(1, min(5, likelihood))
        I = max(1, min(5, impact))
        D = max(1, min(5, detectability))
        R = max(1, min(5, recoverability))
        score = L * I * (6 - D) * (6 - R)
        return score

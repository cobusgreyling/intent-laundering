"""intent-laundering — Test whether your AI safety guardrails are real or cosmetic."""

from intent_laundering.paraphraser import IntentLaunderer
from intent_laundering.tester import SafetyTester
from intent_laundering.scorer import RobustnessScorer
from intent_laundering.report import generate_report

__all__ = [
    "IntentLaunderer",
    "SafetyTester",
    "RobustnessScorer",
    "generate_report",
]

__version__ = "0.1.0"

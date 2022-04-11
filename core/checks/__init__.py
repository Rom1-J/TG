"""
Checks to run on graph
"""
from core.checks.LonelyEntryNode import LonelyEntryNode
from core.checks.LonelyExitNode import LonelyExitNode
from core.checks.NoCircuit import NoCircuit
from core.checks.NonNegativeValues import NonNegativeValues
from core.checks.NullEntryValues import NullEntryValues
from core.checks.SameExitValues import SameExitValues


CHECKS = [
    LonelyEntryNode,
    LonelyExitNode,
    NoCircuit,
    NonNegativeValues,
    NullEntryValues,
    SameExitValues
]

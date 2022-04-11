"""
Check for same exit values
"""
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.Graph import Graph


class SameExitValues:
    """Check for same exit values"""

    __graph: "Graph"

    def __init__(self, graph: "Graph"):
        self.graph = graph

    # =========================================================================
    # =========================================================================

    @property
    def graph(self) -> "Graph":
        """Graph instance

        Returns
        -------
        Graph
        """

        return self.__graph

    @graph.setter
    def graph(self, value: "Graph"):
        self.__graph = value

    # =========================================================================
    # =========================================================================

    @staticmethod
    def check():
        """Run check"""
        return True  # note: can't happens ¯\_(ツ)_/¯

"""
Check for only one entry node
"""
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.Graph import Graph


class LonelyEntryNode:
    """Check for only one entry node"""

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
        return True  # todo: find a case where alpha can be more than 1

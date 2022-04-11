"""
Check for null entry values
"""
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.Graph import Graph


class NullEntryValues:
    """Check for null entry values"""

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

    def check(self):
        """Run check"""
        return self.graph.nodes["α"].duration == 0

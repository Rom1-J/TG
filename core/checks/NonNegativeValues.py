"""
Check for negative arcs values
"""
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.Graph import Graph


class NonNegativeValues:
    """Check for negative arcs values"""

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
        # pylint: disable=use-a-generator
        return not any([n.duration < 0 for n in self.graph.nodes.values()])

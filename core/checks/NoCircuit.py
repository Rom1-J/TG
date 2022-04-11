"""
Check for circuit in graph
"""
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from core.Graph import Graph


class NoCircuit:
    """Check circuit presence"""

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

        nodes = self.graph.nodes.copy()
        # noinspection PyPep8Naming
        ITER = 100

        del nodes["alpha"]
        del nodes["omega"]

        for _ in range(ITER):
            for node in nodes.copy().values():
                has_predecessor = False

                for predecessor in node.predecessors:
                    if (name := predecessor.name) in nodes and name != "alpha":
                        has_predecessor = True

                if not has_predecessor:
                    del nodes[node.name]

            if not nodes:
                break

        return len(nodes) == 0

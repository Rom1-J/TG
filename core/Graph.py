"""
Graph worker
"""
import string
from typing import Dict, List

import numpy as np
from rich.console import Console

from core.checks import CHECKS
from core.Node import Node


ALPHABET = string.ascii_uppercase
console = Console()


class Graph:
    """Represent graph as class object"""

    __predecessors: dict
    __duration: dict

    __nodes: Dict[str, Node]

    __ajd_matrix: np.ndarray
    __val_matrix: np.ndarray

    __ranks: Dict[int, List[Node]]
    __checks_results: Dict[str, List[str]]

    def __init__(self, predecessors: dict, duration: dict):
        self.predecessors = predecessors
        self.duration = duration

        self._generate_nodes()
        self._generate_matrix()

        self.__checks = [check(self) for check in CHECKS]
        self._run_checks()

        if passed := self.checks_results["passed"]:
            console.log("Test %s: [green]✓" % '|'.join(passed))

        if failed := self.checks_results["failed"]:
            console.log("Test %s: [red]✕" % '|'.join(failed))

        if self.checks_results["failed"]:
            console.log("Graph invalide")
        else:
            self._generate_ranks()

            self._generate_earliest()
            self._generate_latest()

    # =========================================================================
    # =========================================================================

    def __str__(self):
        return f"Matrice d'adjacence:\n " \
               f"{self.__render_matrix(self.adj_matrix)}\n" \
               f"Value matrix: \n " \
               f"{self.__render_matrix(self.val_matrix)}"

    # =========================================================================
    # =========================================================================

    def __render_matrix(self, matrix: np.ndarray) -> str:
        out = " " + " ".join(self.nodes) + "\n"

        for i, row in enumerate(matrix):
            out += list(self.nodes.keys())[i] + " "
            out += " ".join(str(el) for el in row)
            out += "\n"

        return out

    # =========================================================================
    # =========================================================================

    @property
    def predecessors(self) -> dict:
        """Dict of predecessors for each node

        Returns
        -------
        dict
        """

        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value: dict):
        self.__predecessors = value

    # =========================================================================

    @property
    def duration(self) -> dict:
        """Dict of duration of each node

        Returns
        -------
        dict
        """

        return self.__duration

    @duration.setter
    def duration(self, value: dict):
        self.__duration = value

    # =========================================================================

    @property
    def nodes(self) -> Dict[str, Node]:
        """Nodes list of this graph

        Returns
        -------
        Dict[str, Node]
        """

        return self.__nodes

    @nodes.setter
    def nodes(self, value: Dict[str, Node]):
        self.__nodes = value

    # =========================================================================

    @property
    def adj_matrix(self) -> np.ndarray:
        """Adjacent matrix representation of this graph

        Returns
        -------
        np.ndarray
        """

        return self.__ajd_matrix

    @adj_matrix.setter
    def adj_matrix(self, value: np.ndarray):
        self.__ajd_matrix = value

    # =========================================================================

    @property
    def val_matrix(self) -> np.ndarray:
        """Value matrix representation of this graph

        Returns
        -------
        np.ndarray
        """

        return self.__val_matrix

    @val_matrix.setter
    def val_matrix(self, value: np.ndarray):
        self.__val_matrix = value

    # =========================================================================

    @property
    def ranks(self) -> Dict[int, List[Node]]:
        """Ranks of this graph

        Returns
        -------
        Dict[int, List[Node]]
        """

        return self.__ranks

    @ranks.setter
    def ranks(self, value: Dict[int, List[Node]]):
        self.__ranks = value

    # =========================================================================

    @property
    def checks_results(self) -> Dict[str, List[str]]:
        """Passed & Failed checks

        Returns
        -------
        Dict[str, List[str]]
        """

        return self.__checks_results

    @checks_results.setter
    def checks_results(self, value: Dict[str, List[str]]):
        self.__checks_results = value

    # =========================================================================
    # =========================================================================

    def _generate_nodes(self):
        nodes: Dict[str, Node] = {
            "α": Node("α", duration=0),
        }

        for node, duration in zip(
                self.predecessors.keys(), self.duration.values()
        ):
            nodes[node] = Node(node, duration=duration)

        nodes["ω"] = Node("ω", duration=0)

        for node, predecessors in self.predecessors.items():
            for predecessor in list(predecessors):
                nodes[node].predecessors.append(nodes[predecessor])
                nodes[predecessor].successors.append(nodes[node])

        for node in nodes.values():
            if not node.predecessors and node.successors:
                nodes["α"].successors.append(node)
                node.predecessors.append(nodes["α"])

            if not node.successors and node.predecessors:
                nodes["ω"].predecessors.append(node)
                node.successors.append(nodes["ω"])

        self.nodes = nodes

    # =========================================================================

    def _generate_matrix(self):
        ajd_matrix = np.zeros((len(self.nodes), len(self.nodes)), dtype=int)
        val_matrix = np.full(
            (len(self.nodes), len(self.nodes)), "*", dtype=str
        )

        for i, node in enumerate(self.nodes.values()):
            if predecessors := node.predecessors:
                for predecessor in predecessors:
                    if predecessor.name == "α":
                        ajd_matrix[i, 0] = 1
                        val_matrix[i, 0] = "0"
                    elif predecessor.name != "ω":
                        ajd_matrix[i, ALPHABET.index(predecessor.name) + 1] = 1
                        val_matrix[
                            i, ALPHABET.index(predecessor.name) + 1
                        ] = str(predecessor.duration)

        self.adj_matrix = ajd_matrix.T
        self.val_matrix = val_matrix.T

    # =========================================================================

    def _generate_ranks(self):
        adj_matrix = self.adj_matrix.copy()
        nodes_indexes = list(self.nodes.values())

        ranks = {}

        while adj_matrix.shape != (0, 0):
            current_rank = []

            # populate ranks
            for i in range(adj_matrix.shape[1]):
                if not any(adj_matrix[:, i]):
                    current_rank.append(i)

            ranks[len(ranks)] = [nodes_indexes[i] for i in current_rank]

            # clean cols/rows
            for i, rank in enumerate(current_rank):
                adj_matrix = np.delete(adj_matrix, rank - i, 0)
                adj_matrix = np.delete(adj_matrix, rank - i, 1)

                del nodes_indexes[rank - i]

        self.ranks = ranks

    # =========================================================================

    def _generate_earliest(self):
        for rank in self.ranks.values():
            for node in rank:
                if predecessors := node.predecessors:
                    node.earliest = max(
                        [p.earliest + p.duration for p in predecessors]
                    )

        self.nodes["ω"].latest = self.nodes["ω"].earliest

    # =========================================================================

    def _generate_latest(self):
        for rank in reversed(self.ranks.values()):
            for node in rank:
                if successors := node.successors:
                    for successor in successors:
                        successor.latest = min([
                            s.latest - successor.duration
                            for s in successor.successors
                        ])

    # =========================================================================
    # =========================================================================

    def _run_checks(self):
        passed = []
        failed = []

        for check in self.__checks:
            name = check.__class__.__name__

            if check.check():
                passed.append(name)
            else:
                failed.append(name)

        self.__checks_results = {"passed": passed, "failed": failed}

    # =========================================================================
    # =========================================================================

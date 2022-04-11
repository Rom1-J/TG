"""
Graph node
"""
from typing import List, Optional


class Node:
    """Graph node"""

    __name: str

    __duration: float

    __predecessors: Optional[List["Node"]]
    __successors: Optional[List["Node"]]

    __earliest: float
    __latest: float

    def __init__(
            self,
            name: str,
            predecessors: Optional[List["Node"]] = None,
            successors: Optional[List["Node"]] = None,
            duration: float = 0.0,
    ):
        self.name = name

        self.predecessors = predecessors or []
        self.successors = successors or []

        self.duration = duration

        self.earliest = 0
        self.latest = 0

    # =========================================================================
    # =========================================================================

    def __repr__(self):
        return f"({self.name}/{self.duration}|" \
               f"p:{''.join(p.name for p in self.predecessors)}|" \
               f"s:{''.join(s.name for s in self.successors)} - " \
               f"e:{self.earliest}|" \
               f"l:{self.latest}|" \
               f"g:{self.gap})"

    __str__ = __repr__

    # =========================================================================
    # =========================================================================

    @property
    def name(self) -> str:
        """Node name"""

        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    # =========================================================================

    @property
    def duration(self) -> float:
        """Node duration"""

        return self.__duration

    @duration.setter
    def duration(self, value: float):
        self.__duration = value

    # =========================================================================

    @property
    def predecessors(self) -> Optional[List["Node"]]:
        """Node predecessors"""

        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value: Optional[List["Node"]]):
        self.__predecessors = value

    # =========================================================================

    @property
    def successors(self) -> Optional[List["Node"]]:
        """Node successors"""

        return self.__successors

    @successors.setter
    def successors(self, value: Optional[List["Node"]]):
        self.__successors = value

    # =========================================================================

    @property
    def earliest(self) -> float:
        """Node earliest time of arrival"""

        return self.__earliest

    @earliest.setter
    def earliest(self, value: float):
        self.__earliest = value

    # =========================================================================

    @property
    def latest(self) -> float:
        """Node latest time of arrival"""

        return self.__latest

    @latest.setter
    def latest(self, value: float):
        self.__latest = value

    # =========================================================================

    @property
    def gap(self):
        """Gap between latest & earliest"""
        return self.latest - self.earliest

    # =========================================================================
    # =========================================================================

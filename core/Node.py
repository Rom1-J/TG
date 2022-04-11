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

    # =========================================================================
    # =========================================================================

    def __repr__(self):
        return f"({self.name}/{self.duration}|" \
               f"p:{''.join(p.name for p in self.predecessors)}|" \
               f"s:{''.join(s.name for s in self.successors)})"

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
    # =========================================================================

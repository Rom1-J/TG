"""
Parse txt file into Graph representation
"""

import string
from typing import Tuple


ALPHABET = string.ascii_uppercase


class Parser:
    """Parse txt file"""

    __file: str

    def __init__(self, file: str):
        self.file = file

    # =========================================================================
    # =========================================================================

    @property
    def file(self) -> str:
        """File from which source to read graph

        Returns
        -------
        str
        """

        return self.__file

    @file.setter
    def file(self, value: str):
        self.__file = value

    # =========================================================================

    def parse(self) -> Tuple[dict, dict]:
        """Parse file

        Returns
        -------
        Tuple[dict, dict]
        """

        predecessors = {}
        weight = {}

        with open(self.file) as f:
            content = f.read().strip()

        for row in content.split("\n"):
            chunks = row.strip().split(" ")

            node = ALPHABET[int(chunks[0]) - 1]

            predecessors[node] = ""
            weight[node] = int(chunks[1])

            if len(chunks) > 2:
                for predec in chunks[2:]:
                    predecessors[node] += ALPHABET[int(predec) - 1]

        return predecessors, weight

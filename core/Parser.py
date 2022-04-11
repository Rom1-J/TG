"""
Parse txt file into Graph representation
"""

import string
from typing import Tuple


ALPHABET = string.ascii_uppercase


class Parser:
    """Parse txt file"""

    __file: str

    __predecessors: dict
    __duration: dict

    def __init__(self, file: str):
        self.__file = file

    # =========================================================================
    # =========================================================================

    def parse(self):
        """Parse file"""

        predecessors = {}
        duration = {}

        with open(self.__file) as f:
            content = f.read().strip()

        for row in content.split("\n"):
            chunks = row.strip().split(" ")

            node = ALPHABET[int(chunks[0]) - 1]

            predecessors[node] = ""
            duration[node] = int(chunks[1])

            if len(chunks) > 2:
                for pred in chunks[2:]:
                    predecessors[node] += ALPHABET[int(pred) - 1]

        self.__predecessors = predecessors
        self.__duration = duration

    # =========================================================================

    def dump(self) -> Tuple[dict, dict]:
        """Dump parsed data

        Returns
        -------
        Tuple[dict, dict]
            predecessors, duration
        """
        return self.__predecessors, self.__duration

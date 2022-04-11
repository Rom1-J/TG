"""
App
"""
from pprint import pprint

from core.Graph import Graph
from core.Parser import Parser


def main():
    """Main function"""

    parser = Parser("data/table 5.txt")
    parser.parse()

    graph = Graph(*parser.dump())
    pprint(list(graph.nodes.values()))


if __name__ == "__main__":
    main()

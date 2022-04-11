"""
App
"""

from core.Graph import Graph
from core.Parser import Parser


def main():
    """Main function"""

    parser = Parser("data/table 3.txt")
    parser.parse()

    graph = Graph(*parser.dump())

    print(graph)

    graph.print_checks()
    graph.print_ranks()


if __name__ == "__main__":
    main()

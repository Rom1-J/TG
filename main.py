"""
App
"""

from core.Parser import Parser
from core.Graph import Graph


def main():
    """Main function"""

    parser = Parser("data/table 3.txt")
    parser.parse()

    graph = Graph(*parser.dump())

    print(graph)
    graph.checks()


if __name__ == "__main__":
    main()

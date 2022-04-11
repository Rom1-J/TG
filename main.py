"""
App
"""

from core.Graph import Graph
from core.Parser import Parser


def main():
    """Main function"""

    parser = Parser("data/table 5.txt")
    parser.parse()

    graph = Graph(*parser.dump())
    print(graph)


if __name__ == "__main__":
    main()

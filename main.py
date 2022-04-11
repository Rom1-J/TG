"""
App
"""

from core.parser import Parser


def main():
    """Main function"""

    parser = Parser("data/table 5.txt")
    p, w = parser.parse()

    print(p)
    print(w)


if __name__ == "__main__":
    main()

"""
App
"""
from pprint import pprint

from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt

from core.Graph import Graph
from core.Parser import Parser

console = Console()


def main():
    """Main function"""

    while (prompt := IntPrompt.ask(
            "Choisissez un graph (entrer pour quitter): ",
            choices=[f"{i}" for i in range(1, 13)],
            default="exit"
    )) != "exit":
        console.clear()
        graph_name = f"table {prompt}.txt"

        console.log("Chargement de '%s'" % graph_name)

        parser = Parser(f"data/{graph_name}")
        parser.parse()

        graph = Graph(*parser.dump())

        console.print("\n")
        console.print(graph)

        if not graph.checks_results["failed"]:
            table = Table(title="Informations")

            table.add_column("Rangs: (%d)" % len(graph.ranks))
            table.add_column("Dates au plus tôt")
            table.add_column("Dates au plus tard")
            table.add_column("Marges")

            rank_rows = []
            for i, rank in graph.ranks.items():
                rank_rows.append(
                    "%d: sommets %s" % (i, " ".join(r.name for r in rank))
                )

            earliest_rows = []
            latest_rows = []
            gap_rows = []
            for node in graph.nodes.values():
                earliest_rows.append("%s: %d" % (node.name, node.earliest))
                latest_rows.append("%s: %d" % (node.name, node.latest))
                gap_rows.append("%s: %d" % (node.name, node.gap))

            if len(rank_rows) > len(earliest_rows):
                diff = len(rank_rows) - len(earliest_rows)

                earliest_rows.extend(["" for _ in range(diff)])
                latest_rows.extend(["" for _ in range(diff)])
                gap_rows.extend(["" for _ in range(diff)])
            elif len(rank_rows) < len(earliest_rows):
                diff = len(earliest_rows) - len(rank_rows)

                rank_rows.extend(["" for _ in range(diff)])

            for i, rank_row in enumerate(rank_rows):
                table.add_row(
                    rank_row, earliest_rows[i], latest_rows[i], gap_rows[i]
                )

            console.print(table)


if __name__ == "__main__":
    main()

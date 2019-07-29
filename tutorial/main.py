from graphs.graph import fill_graph
from graphs.utils.file_reader import read_graph_file


def main():
    graph, vertices, edges = read_graph_file("inputs/insanegraph.txt")

    fill_graph(graph, vertices, edges)
    print(graph.clique())


if __name__ == "__main__":
    main()

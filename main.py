import networkx as nx
import matplotlib.pyplot as plt
import random
import os
import time


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = set()

    def add_edge(self, u, v):
        edge = (min(u, v), max(u, v))

        if u != v and edge not in self.edges:
            self.edges.add(edge)

    def is_vertex_cover(self, vertices):
        vertex_set = set(vertices)

        for u, v in self.edges:
            if u not in vertex_set and v not in vertex_set:
                return False

        return True

    def min_vertex_cover(self):
        min_cover = None
        min_size = self.V + 1

        for mask in range(1 << self.V):
            current_cover = []

            for i in range(self.V):
                if mask & (1 << i):
                    current_cover.append(i)

            if len(current_cover) >= min_size:
                continue

            if self.is_vertex_cover(current_cover):
                min_cover = current_cover
                min_size = len(current_cover)

        return min_size, min_cover

    def generate_subsets(self, index, current, file):
        if index == self.V:
            print(current)
            return

        current.append(index)
        self.generate_subsets(index + 1, current, file)
        current.pop()
        self.generate_subsets(index + 1, current, file)


def genGraph(n, m):
    max_edges = n * (n - 1) // 2

    if m > max_edges:
        raise ValueError(
            f"maximum possible edges for {n} vertices is {max_edges}"
        )

    graph = Graph(n)
    while len(graph.edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            graph.add_edge(u, v)

    return graph


os.makedirs("output", exist_ok=True)
n = 10
m_values = [10, 20, 30, 40, 45]

for m in m_values:
    graph = genGraph(n, m)
    start_time = time.perf_counter()
    min_size, min_cover = graph.min_vertex_cover()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    filename = f"output/n{n}_m{m}.txt"
    with open(filename, "w") as file:

        file.write(f"n = {n}\n")
        file.write(f"m = {m}\n\n")

        file.write("Graph edges:\n")

        for edge in sorted(graph.edges):
            file.write(str(edge) + "\n")

        file.write("\nMinimum Vertex Cover:\n")
        file.write(f"Size = {min_size}\n")
        file.write(f"Vertices = {min_cover}\n")

        file.write("\nAlgorithm Execution Time:\n")
        file.write(f"{execution_time:.10f} seconds\n")

        file.write("\nAll possible subsets:\n")

        graph.generate_subsets(0, [], file)

    print(f"Saved: {filename}")
    print(f"Minimum Vertex Cover Size: {min_size}")
    print(f"Execution Time: {execution_time:.10f} seconds")
    print("-" * 50)

    G = nx.Graph()
    G.add_nodes_from(range(graph.V))
    G.add_edges_from(graph.edges)

    cover_set = set(min_cover)

    node_colors = []

    for node in G.nodes():
        if node in cover_set:
            node_colors.append("red")
        else:
            node_colors.append("skyblue")

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        with_labels=True,
        node_size=1500,
        font_size=12,
        node_color=node_colors,
        edge_color="black"
    )

    plt.title(
        f"Minimum Vertex Cover (n={n}, m={m}, size={min_size})"
    )

    plt.show()
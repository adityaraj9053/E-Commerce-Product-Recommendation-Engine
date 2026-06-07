import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(co):

    G = nx.Graph()

    for u, neighbors in co.graph.items():
        for v, w in neighbors.items():
            G.add_edge(u, v, weight=w)

    plt.figure(figsize=(12, 8))

    nx.draw(
        G,
        with_labels=True,
        node_size=500,
        font_size=8
    )

    plt.savefig("images/co_occurrence_graph.png")
    plt.show()
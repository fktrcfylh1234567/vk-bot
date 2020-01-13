import itertools

import networkx as nx
import matplotlib.pyplot as plt


def make_graph(graph):
    g = nx.Graph(directed=False)

    for i in graph:
        g.add_node(i)

    friends = tuple(graph.keys())
    print(friends)

    for (i, j) in itertools.combinations(range(len(graph.keys())), 2):
        i = friends[i]
        j = friends[j]
        if i in graph[j]:
            g.add_edge(i, j)

    return g


def display(graph, labels):
    g = make_graph(graph)
    pos = nx.spring_layout(g)

    nx.draw(g, pos=pos, node_size=30, with_labels=False, width=0.2)
    nx.draw_networkx_labels(g, pos, labels)
    plt.show()

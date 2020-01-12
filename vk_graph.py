import networkx as nx
import matplotlib.pyplot as plt


def display(graph, friends, labels):
    g = nx.Graph(directed=False)
    for i in graph:
        g.add_node(i)
        for j in graph[i]:
            if i != j and i in friends and j in friends:
                g.add_edge(i, j)

    pos = nx.spring_layout(g)

    nx.draw(g, pos=pos, node_size=30, with_labels=False, width=0.2)
    nx.draw_networkx_labels(g, pos, labels)
    plt.show()


def save(graph, friends):
    g = nx.Graph(directed=False)
    for i in graph:
        g.add_node(i)
        for j in graph[i]:
            if i != j and i in friends and j in friends:
                g.add_edge(i, j)

    nx.draw(g, node_size=30, with_labels=False, width=0.2)
    plt.gcf().set_size_inches(50, 50)
    plt.savefig('file.png')

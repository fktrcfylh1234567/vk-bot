import itertools

import networkx as nx
import matplotlib.pyplot as plt


def make_graph(friends):
    g = nx.Graph(directed=False)

    for fr in friends:
        g.add_node(fr['id'])

    for (i, j) in itertools.combinations(range(len(friends)), 2):
        if friends[i]['id'] in friends[j]['friends']:
            w = len(list(set(friends[i]['friends']) & set(friends[j]['friends'])))
            g.add_edge(friends[i]['id'], friends[j]['id'], weight=w * 10000)

    return g


def display(friends):
    g = make_graph(friends)
    pos = nx.spring_layout(g)

    labels = dict()

    for user in friends:
        labels[user['id']] = user['first_name'] + " " + user['last_name']

    nx.draw(g, pos=pos, node_size=30, with_labels=False, width=0.2)
    nx.draw_networkx_labels(g, pos, labels)
    plt.show()

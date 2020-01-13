import ast


def read_data_from_files():
    graph = open('graph.json', 'r').readline()
    labels = open('names.json', 'r').read()

    graph = ast.literal_eval(graph)
    labels = ast.literal_eval(labels)

    return graph, labels


def save_data_to_files(graph, labels):
    graph_file = open('graph.json', 'w')
    labels_file = open('names.json', 'w')

    graph_file.write(str(graph))
    labels_file.write(str(labels))

    graph_file.close()
    labels_file.close()

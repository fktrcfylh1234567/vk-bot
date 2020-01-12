import ast


def read_data_from_files():
    graph = open('graph.json', 'r').readline()
    friends = open('friends.json', 'r').readline()
    labels = open('names.json', 'r').read()

    graph = ast.literal_eval(graph)
    friends = ast.literal_eval(friends)
    labels = ast.literal_eval(labels)

    return graph, friends, labels


def save_data_to_files(graph, friends, labels):
    graph_file = open('graph.json', 'w')
    friends_file = open('friends.json', 'w')
    labels_file = open('names.json', 'w')

    graph_file.write(str(graph))
    friends_file.write(str(friends))
    labels_file.write(str(labels))

    graph_file.close()
    friends_file.close()
    labels_file.close()

import ast


def read_data_from_file():
    graph = open('data.json', 'r').readline()
    graph = ast.literal_eval(graph)
    return graph


def save_data_to_file(data):
    graph_file = open('data.json', 'w')
    graph_file.write(str(data))
    graph_file.close()

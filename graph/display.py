from graph.files import read_data_from_files
from graph.vk_graph import display

(graph, labels) = read_data_from_files()
display(graph, labels)

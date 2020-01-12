from files import read_data_from_files
from vk_graph import display

(graph, friends, labels) = read_data_from_files()
display(graph, friends, labels)

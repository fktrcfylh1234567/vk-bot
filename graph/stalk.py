from graph.files import save_data_to_files
from graph.grep import get_user_graph, get_user_id_by_name
from graph.vk_graph import display

user_id = get_user_id_by_name('')
(graph, labels) = get_user_graph(user_id)
save_data_to_files(graph, labels)

display(graph, labels)

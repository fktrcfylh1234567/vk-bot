from files import save_data_to_files
from grep import make_graph, get_user_id_by_name
from vk_graph import display

user_id = get_user_id_by_name('')
(graph, friends, labels) = make_graph(user_id)
save_data_to_files(graph, friends, labels)

display(graph, friends, labels)

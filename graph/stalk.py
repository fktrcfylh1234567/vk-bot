from graph.files import save_data_to_file
from graph.grep import get_user_graph, get_user_id_by_name

user_id = get_user_id_by_name('')
data = get_user_graph(user_id)
save_data_to_file(data)

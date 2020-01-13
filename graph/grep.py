from copy import copy

from vk_auth import vk


def get_user_id_by_name(user_name):
    res = vk.users.get(user_ids=user_name)
    return res[0]['id']


def get_user_name(user_id):
    res = vk.users.get(user_id=user_id)
    return res[0]['first_name'] + " " + res[0]['last_name']


def get_user_photo(user_id):
    res = vk.users.get(user_id=user_id, fields='photo')
    return res['photo']


def get_user_education(user_id):
    res = vk.users.get(user_id=user_id, fields='education, universities, schools')
    return res['photo']


def get_friends(user_id):
    return vk.friends.get(user_id=user_id)


def get_mutual_friends(source_uid, target_uid):
    return vk.friends.getMutual(source_uid=source_uid, target_uid=target_uid)


def get_user_graph(user_id):
    graph = {}
    friends = get_friends(user_id)['items']
    friends_non_private = copy(friends)

    for friend_id in friends:
        try:
            graph[friend_id] = get_friends(friend_id)['items']
        except BaseException:
            friends_non_private.remove(friend_id)

    labels = dict()
    for friend_id in friends_non_private:
        labels[friend_id] = get_user_name(friend_id)

    return graph, labels

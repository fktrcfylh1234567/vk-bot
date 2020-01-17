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
    res = vk.users.get(user_id=user_id, fields='education')
    return res['photo']


def get_friends(user_id):
    return vk.friends.get(user_id=user_id)


def get_friends_edu(user_id):
    return vk.friends.get(user_id=user_id, fields='education')


def get_mutual_friends(source_uid, target_uid):
    return vk.friends.getMutual(source_uid=source_uid, target_uid=target_uid)


def get_user_graph(user_id):
    friends = get_friends_edu(user_id)['items']
    friends = list(filter(lambda f: not f['is_closed'], friends))

    for friend in friends:
        friend['friends'] = get_friends(friend['id'])['items']

    return friends

import os


def get_vk_token():
    return os.environ['vk_token']


def get_bot_group_id():
    return os.environ['bot_group_id']


def get_admin_id():
    return os.environ['admin_id']


def get_phone_number():
    return os.environ['phone_number']


def get_password():
    return os.environ['password']

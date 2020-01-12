import vk_api
from env import get_phone_number, get_password

phone_number = get_phone_number()
password = get_password()

vk_session = vk_api.VkApi(phone_number, password)
vk_session.auth()
vk = vk_session.get_api()

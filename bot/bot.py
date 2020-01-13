import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

from env import get_vk_token, get_bot_group_id, get_admin_id
from bot.title import get_true_group_title

token = get_vk_token()
group_id = get_bot_group_id()
admin_id = get_admin_id()

print("vk_token: " + token)
print("bot_group_id: " + group_id)
print("admin_id: " + admin_id)

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id)

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:

        # LS message
        if event.object.from_id == event.object.peer_id:
            print("Bot direct message from ", end='')
            print(event.obj.from_id)

            if len(event.obj.attachments) == 0:
                print('Текст:', event.obj.text, "\n")
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=("Новое сообщение - " + event.obj.text)
                )

            elif event.obj.attachments[0]['type'] == 'sticker':
                product_id = event.obj.attachments[0]['sticker']['product_id']
                sticker_id = event.obj.attachments[0]['sticker']['sticker_id']
                print('sticker:', product_id, sticker_id, "\n")

                if product_id == 4 and sticker_id == 163:
                    msg = 'Stiker Allowed'
                else:
                    msg = 'Stiker Not Allowed!'

                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=msg
                )

    # Confa message
    elif event.object.text != '':
        print("Confa message from ", end='')
        print(event.object.from_id)
        print('Текст:', event.obj.text, "\n")

    # Actions
    elif hasattr(event.object, 'action'):

        # Title Changed
        if event.object.action['type'] == 'chat_title_update':
            print("Title Changed", "\n")

            true_title = get_true_group_title()
            chat_id = int(event.object.peer_id) - 2000000000
            vk.messages.editChat(chat_id=chat_id, title=true_title)

        else:
            print("action: ", event.object.action['type'], "\n")
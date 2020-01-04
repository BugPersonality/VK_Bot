import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Начать игру', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Движение вверх', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('Движение влево', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Движение вправо', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Движение вниз', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('Закончить игру', color=VkKeyboardColor.POSITIVE)
























# import vk_api
# from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
# import json
#
# def get_button(lable, color, payload=""):
#     return {
#         "action": {
#             "type": "text",
#             "payload": json.dumps(payload),
#             "lable": lable
#         },
#         "color": color
#     }
#
# keyboard = {
#     "one_time": False,
#     "buttons": [
#         [
#             get_button(lable="вверх", color="Primary"),
#             get_button(lable="вниз", color="Positive"),
#             get_button(lable="влево", color="Negative"),
#             get_button(lable="вправо", color="Secondary")
#         ]
#     ]
# }
#
# keyboard = {
#     "one_time": False,
#     "buttons": [
#         [{
#             "action": {
#                 "type": "text",
#                 "payload": "{\"button\": \"1\"}",
#                 "label": "влево"
#             },
#             "color": "Negative"
#         },
#             {
#                 "action": {
#                     "type": "text",
#                     "payload": "{\"button\": \"2\"}",
#                     "label": "вниз"
#                 },
#                 "color": "Positive"
#             },
#             {
#                 "action": {
#                     "type": "text",
#                     "payload": "{\"button\": \"2\"}",
#                     "label": "вверх"
#                 },
#                 "color": "Primary"
#             },
#             {
#                 "action": {
#                     "type": "text",
#                     "payload": "{\"button\": \"2\"}",
#                     "label": "вправо"
#                 },
#                 "color": "Secondary"
#             }
#         ]
#     ]
# }
#
# keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
# keyboard = str(keyboard.decode('utf-8'))


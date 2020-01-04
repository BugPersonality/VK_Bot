from flask import Flask, request, json
from gtts import gTTS
from libraly import *
from bs4 import BeautifulSoup
from get_timme import *
from game_2048 import *
from buttons import *
from user_information import *

def get_buttons():
    return vk.method("messages.send", {
                    "peer_id": id,
                    "random_id": get_random_id(),
                    "keyboard": keyboard.get_keyboard(),
                    "message": 'Клавиатура'
                })

def get_html(url):
    response = requests.get(url)
    return response.text

def text_before_word(text, word):
    line = text.split(word)[0].strip()
    return line

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        price = text_before_word(soup.find('span',
            class_='cmc-details-panel-price__price').text, 'USD')
    except:
        price = ''
    data = ["bitcoin", price]
    return data

token = "Ваш токен нужно записать здесь"
vk = vk_api.VkApi(token=token)
vk._auth_token()

matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
l = "-------------------"
print("Я уже смторю в вк")

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})

        if messages["count"] >= 1:

            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            words = []
            words.append(body)
            split_words = []
            split_words = words[0].split()

            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет, кст я знаю адресс твоей странички: "
                                                     "\n https://vk.com/id" + str(id), "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "время":
                time_n = get_time()
                vk.method("messages.send",
                          {"peer_id": id, "message": "Текущее время в Питере:"
                                                     "\n" + str(time_n) + "\n"+l+"\nвзято с сайта: \n\nhttps://my-calend.ru/date-and-time-today",
                           "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "курс биткоина":
                html = get_html("https://coinmarketcap.com/currencies/bitcoin/")
                data = get_page_data(html)
                rate = data
                print(rate)
                vk.method("messages.send",
                          {"peer_id": id, "message": "Текущий курс Биткоина : " + str(rate[1]) +"\nвзято с сайта:  \n"
                                                     "https://coinmarketcap.com/currencies/bitcoin/", "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "поема":
                poem = """"""
                for sentence in get_poem():
                    poem += sentence
                vk.method("messages.send",
                          {"peer_id": id, "message":"Каждый раз я генерирую разные стихи, "
                                                    "если вам не понравилось мое творение, "
                                                    "то дайте мне еще шанс\n"+ l +"\n"
                                                                                  "кст он научил меня писат "
                                                                                  "стихи\n\nhttps://vk.com/id514591816\n" + l + "\n"
                                                                                 + poem, "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "срать":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Это вам не Муниципальный туалет на Дыбенко срать надо тут: \n"
                                                     "https://vk.com/tk_dybenko", "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "картинка "+split_words[1]:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Вот ссылка на картинки по вашему запросу: \n"
                                                     "https://ru.depositphotos.com/stock-photos/"+split_words[1]+".html?filter=all",
                           "random_id": random.randint(1, 2147483647)})


            elif body.lower() == "закончить игру":
                end_game(id)
                matrix_end = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": f"Ваша карта в конце\n{'  '.join(map(str, matrix_end[0]))}\n{'  '.join(map(str, matrix_end[1]))}\n{'  '.join(map(str, matrix_end[2]))}\n{'  '.join(map(str, matrix_end[3]))}",
                           "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "начать игру":
                matrix = check_user(id)
                matrix = put_number(matrix)
                update_user(id, matrix)
                get_buttons()
                vk.method("messages.send",
                          {"peer_id": id, "message": f"Ваша карта в начале игры\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                           "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "движение вправо":
                get_buttons()
                if check_matrix(matrix) == "win":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы победили\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "lose":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы проиграли\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "continue":
                    matrix = get_matrix(id)
                    matrix = right(matrix)
                    update_user(id, matrix)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы сделали движение вправо\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "движение влево":
                get_buttons()
                if check_matrix(matrix) == "win":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы победили\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "lose":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы проиграли\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "continue":
                    matrix = get_matrix(id)
                    matrix = left(matrix)
                    update_user(id, matrix)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы сделали движение влево\nВот Вашa карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})


            elif body.lower() == "движение вниз":
                get_buttons()
                if check_matrix(matrix) == "win":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы победили\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "lose":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы проиграли\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "continue":
                    matrix = get_matrix(id)
                    matrix = down(matrix)
                    update_user(id, matrix)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы сделали движение вниз\nВот Ваши карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})


            elif body.lower() == "движение вверх":
                get_buttons()
                if check_matrix(matrix) == "win":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы победили\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "lose":
                    matrix = get_matrix(id)
                    end_game(id)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы проиграли\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

                elif check_matrix(matrix) == "continue":
                    matrix = get_matrix(id)
                    matrix = up(matrix)
                    update_user(id, matrix)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": f"Вы сделали движение вверх \n Вот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}",
                               "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "!Я тебя не понимаю, напиши что-нибудь из списка команд!\n"
                                                     "Вот список команд: \n\n"
                                                     "1) Привет\n "
                                                     "2) Поема\n"
                                                     "3) Срать\n"
                                                     "4) Время\n"
                                                     " 5) Курс Биткоина\n"
                                                     "6)Картика _название_вашей_картинки_\n"
                                                     "7)Начать игру \n"
                                                     , "random_id": random.randint(1, 2147483647)})

    except Exception as E:
        time.sleep(1)
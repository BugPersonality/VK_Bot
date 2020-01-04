import sqlite3 as sql3
import random
import vk_api

def end_game(id):

    conn = sql3.connect("matrixDB.db")
    cursor = conn.cursor()

    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matrix_new = matrix_to_list(matrix)

    cursor.execute(f"UPDATE user_information SET matrix = '{matrix_new}' WHERE id = '{id}' ")
    conn.commit()

    cursor.close()
    conn.close()


def add_user(id):

    matrix_inf = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    conn = sql3.connect("matrixDB.db")
    cursor = conn.cursor()

    matrix_inf = matrix_to_list(matrix_inf)

    cursor.execute(f"""INSERT INTO user_information (id, matrix) VALUES ("{id}", "{matrix_inf}")""")
    conn.commit()

    cursor.close()
    conn.close()


def get_matrix(id):
    conn = sql3.connect("matrixDB.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT matrix FROM user_information WHERE id = "{id}" """)

    data = cursor.fetchall()[0][0].split(',')

    cursor.close()
    conn.close()

    return list_to_matrix(data)


def update_user(id, matrix):

    conn = sql3.connect("matrixDB.db")
    cursor = conn.cursor()

    matrix_new = matrix_to_list(matrix)

    cursor.execute(f"UPDATE user_information SET matrix = '{matrix_new}' WHERE id = '{id}' ")
    conn.commit()

    cursor.close()
    conn.close()


def check_user(id):
    token = "Ваш токен нужно записать здесь"
    vk = vk_api.VkApi(token=token)
    vk._auth_token()

    conn = sql3.connect("matrixDB.db")
    cursor = conn.cursor()

    cursor.execute(f'''SELECT id FROM user_information  WHERE id = "{id}"''')
    row = cursor.fetchone()

    if not(row):
        add_user(id)
        vk.method("messages.send",
                  {"peer_id": id,
                   "message": f"Поздравляю, вы успешно зарегестрированы ваш id = {id}",
                   "random_id": random.randint(1, 2147483647)})
        print("успешно зарегал")
        cursor.close()
        conn.close()
        return get_matrix(id)

    else:
        cursor.close()
        conn.close()
        return get_matrix(id)


def matrix_to_list(matrix):
    list = []
    for i in range(4):
        for j in range(4):
            list.append(matrix[i][j])

    buffer = ""

    for x in list:
        buffer += f",{x}"

    buffer = buffer[1:]

    return buffer


def list_to_matrix(array):
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    k = 0
    for i in range(4):
        for j in range(4):
            matrix[i][j] = int(array[k])
            if k <= 15:
                k += 1
            else:
                break

    return matrix

#user_information

# conn = sql3.connect("matrixDB.db")
# cursor = conn.cursor()
#
# matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# list_ = matrix_to_list(matrix)
# buffer_ = ""
#
# for x in list_:
#     buffer_ += f",{x}"
#
# cursor.execute(f"""INSERT INTO user_information VALUES("{123}", "{buffer_}")""")
# conn.commit()
#
# cursor.close()
# conn.close()


# matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# print(f"Вы победили\nВот Ваша карта:\n{'  '.join(map(str, matrix[0]))}\n"
#       f"{'  '.join(map(str, matrix[1]))}\n{'  '.join(map(str, matrix[2]))}\n{'  '.join(map(str, matrix[3]))}")

# db = sqlite3.connect("matrixDB.db")
# cur = db.cursor()
#
# need_id = 123
# cur.execute(f"""SELECT matrix FROM user_information WHERE id = "{need_id}" """)
#
# data = cur.fetchall()[0][0].split(',')
# del data[0]
# print(data)
# print(len(data))

# list = []
# for i in range(4):
#     for j in range(4):
#         list.append(matrix[i][j])
# buffer = ""
#
# for x in list:
#     buffer += f",{x}"
# print(buffer)
# buffer = buffer[1:]
# print(buffer)
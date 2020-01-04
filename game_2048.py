import random

def matrix_print(matrix):
    k = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                print(".", end="    ")
                k = k + 1
            elif matrix[i][j] > 0:
                print(str(matrix[i][j]), end="    ")
                k = k + 1
        if k == 4 or k == 8 or k == 12 or k == 16:
            print("\n")

def check_matrix(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return "win"

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return "continue"

    for i in range(4):
        for j in range(0, 4):
            if i != 3 and j != 3:
                if matrix[i][j] == matrix[i + 1][j] or matrix[i][j] == matrix[i][j + 1]:
                    return "continue"
            if j == 3 and i != 3:
                if matrix[i][j] == matrix[i - 1][j]:
                    return "continue"
            if i == 3 and j != 3:
                if matrix[i][j] == matrix[i + 1][j]:
                    return "continue"
    return "lose"


def put_number(matrix):
    for k in range(200):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        number = random.randrange(2, 5, 2)

        if matrix[i][j] == 0:
            matrix[i][j] = number
            return matrix


def left(matrix):
    move = False

    for i in range(4):
        for j in range(1, 4):
            if matrix[i][j] > 0:
                while matrix[i][j - 1] == 0 and (j - 1 > - 1):
                    matrix[i][j - 1] = matrix[i][j]
                    matrix[i][j] = 0
                    j = j - 1
                    move = True

    for i in range(4):
        for j in range(1, 4):
            if matrix[i][j] > 0:
                if matrix[i][j] == matrix[i][j - 1]:
                    matrix[i][j - 1] = matrix[i][j] * 2
                    if j <= 2:
                        while (matrix[i][j + 1] > 0) and (j <= 2) and (j >= 0):
                            matrix[i][j] = matrix[i][j + 1]
                            move = True
                            if j + 1 <= 2:
                                j = j + 1
                            else:
                                break
                        matrix[i][j] = 0

    if move == True:
        matrix = put_number(matrix)
    return matrix


def right(matrix):
    move = False
    for i in range(4):
        for j in range(len(matrix) - 2, -1, -1):
            if matrix[i][j] != 0:
                while (matrix[i][j + 1] == 0) and (j <= 2) and (j >= 0):
                    matrix[i][j + 1] = matrix[i][j]
                    matrix[i][j] = 0
                    move = True
                    if j + 1 <= 2:
                        j = j + 1
                    else:
                        break

    for i in range(4):
        for j in range(len(matrix) - 2, -1, -1):
            if matrix[i][j] > 0:
                if matrix[i][j + 1] == matrix[i][j]:
                    matrix[i][j + 1] = matrix[i][j] * 2
                    if j >= 1:
                        while matrix[i][j - 1] > 0:
                            matrix[i][j] = matrix[i][j - 1]
                            move = True
                            if j >= 1:
                                j = j - 1
                            else:
                                break
                        matrix[i][j] = 0

    if move == True:
        matrix = put_number(matrix)
    return matrix

def up(matrix):
    move = False
    for j in range(4):
        for i in range(1, 4):
            if matrix[i][j] > 0:
                while (matrix[i - 1][j] == 0) and (i - 1 >= 0):
                    matrix[i - 1][j] = matrix[i][j]
                    matrix[i][j] = 0
                    move = True
                    if i >= 1:
                        i = i - 1
                    else:
                        break

    for j in range(4):
        for i in range(1, 4):
            if matrix[i][j] > 0:
                if matrix[i - 1][j] == matrix[i][j]:
                    matrix[i - 1][j] = matrix[i][j] * 2
                    if i <= 1:
                        while matrix[i + 1][j] > 0 and i <= 2:
                            matrix[i][j] = matrix[i - 1][j]
                            move = True
                            if i <= 2:
                                i = i + 1
                            else:
                                break
                        matrix[i][j] = 0

    if move == True:
        matrix = put_number(matrix)
    return matrix

def down(matrix):
    move = False
    for j in range(4):
        for i in range(2, -1, -1):
            if matrix[i][j] > 0:
                while (matrix[i + 1][j] == 0) and (i <= 2):
                    matrix[i + 1][j] = matrix[i][j]
                    matrix[i][j] = 0
                    move = True
                    if i + 1 <= 2:
                        i = i + 1
                    else:
                        break

    for j in range(4):
        for i in range(2, -1, -1):
            if matrix[i][j] > 0:
                if matrix[i + 1][j] == matrix[i][j]:
                    matrix[i + 1][j] = matrix[i][j] * 2
                    if i >= 1:
                        while matrix[i - 1][j] > 0 and (i - 1 >= 0):
                            matrix[i][j] = matrix[i - 1][j]
                            move = True
                            if i <= 1:
                                i = i - 1
                            else:
                                break
                        matrix[i][j] = 0

    if move == True:
        matrix = put_number(matrix)
    return matrix

# matrix = [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0]]

# flag = True
# while flag:
#     command = input()
#     if command == "l":
#
#         if check_matrix(matrix) == "win":
#             print("win")
#             matrix_print(matrix)
#
#         elif check_matrix(matrix) == "lose":
#             print("lose")
#             matrix_print(matrix)
#             flag = False
#
#         elif check_matrix(matrix) == "continue":
#             matrix = left(matrix)
#             print("continue")
#             matrix_print(matrix)
#
#     elif command == "r":
#
#         if check_matrix(matrix) == "win":
#             print("win")
#             matrix_print(matrix)
#
#         elif check_matrix(matrix) == "lose":
#             print("lose")
#             matrix_print(matrix)
#             flag = False
#
#         elif check_matrix(matrix) == "continue":
#             matrix = right(matrix)
#             print("continue")
#             matrix_print(matrix)
#
#     elif command == "u":
#
#         if check_matrix(matrix) == "win":
#             print("win")
#             matrix_print(matrix)
#
#         elif check_matrix(matrix) == "lose":
#             print("lose")
#             matrix_print(matrix)
#             flag = False
#
#         elif check_matrix(matrix) == "continue":
#             matrix = up(matrix)
#             print("continue")
#             matrix_print(matrix)
#
#     elif command == "d":
#
#         if check_matrix(matrix) == "win":
#             print("win")
#             matrix_print(matrix)
#
#         elif check_matrix(matrix) == "lose":
#             print("lose")
#             matrix_print(matrix)
#             flag = False
#
#         elif check_matrix(matrix) == "continue":
#             matrix = down(matrix)
#             print("continue")
#             matrix_print(matrix)

            # for i in range(4):
            #     print(" ".join(map(str, matrix[i])))


# flag = True
# while flag:
#
#     if check_matrix(matrix) == "win":
#         flag = False
#         print("вы победили")
#
#     elif check_matrix(matrix) == "lose":
#         flag = False
#         print("вы проиграли")
#
#     elif check_matrix(matrix) == "continue":
#         print("Введите команду")
#         answer = input()
#         if answer == "u":
#             move = False
#             matrix = up(matrix)
#             print("Состояние игры : \n" + str(matrix[0]) +
#                   "\n" + str(matrix[1]) + "\n" + str(matrix[2]) + "\n" + str(matrix[3]) + "\n")
#
#         elif answer == "d":
#             move = False
#             matrix = down(matrix)
#             print("Состояние игры : \n" + str(matrix[0]) +
#                   "\n" + str(matrix[1]) + "\n" + str(matrix[2]) + "\n" + str(matrix[3]) + "\n")
#
#         elif answer == "l":
#             move = False
#             matrix = left(matrix)
#             print("Состояние игры : \n" + str(matrix[0]) +
#                   "\n" + str(matrix[1]) + "\n" + str(matrix[2]) + "\n" + str(matrix[3]) + "\n")
#
#         elif answer == "r":
#             move = False
#             matrix = right(matrix)
#             print("Состояние игры : \n" + str(matrix[0]) +
#                   "\n" + str(matrix[1]) + "\n" + str(matrix[2]) + "\n" + str(matrix[3]) + "\n")
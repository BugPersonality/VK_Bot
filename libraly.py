import sqlite3, random, time

def rifm():
    global words
    first_word = "0"
    second_word = "1"
    while True:
        if first_word[-3:] == second_word[-3:] and first_word != second_word:
            return [first_word, second_word]
        first_word = words[random.randint(0, len(words) - 1)]
        second_word = words[random.randint(0, len(words) - 1)]

def get_poem():
    global db, cur, words
    poem = []
    array = []
    array.extend(rifm())
    array.extend(rifm())
    for i in range(4):
        poem.append("")
        for j in range(3):
            poem[-1] += f""" {words[random.randint(0, len(words) - 1)]}"""
        poem[-1] += f""" {array[i]}\n"""

    return poem

db = sqlite3.connect("awesome.db")
cur = db.cursor()
cur.execute("""SELECT word FROM WORDS WHERE word != "" """)

words = cur.fetchall()
words = [x[0] for x in words]
import bs4
import requests

def get_time():
    request = requests.get("https://my-calend.ru/date-and-time-today")
    b = bs4.BeautifulSoup(request.text, "html.parser")
    return clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

def clean_all_tag_from_str(string_line):
    result = ""
    not_skip = True
    for i in list(string_line):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True

    return result
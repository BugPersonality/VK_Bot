from bs4 import BeautifulSoup
import requests

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
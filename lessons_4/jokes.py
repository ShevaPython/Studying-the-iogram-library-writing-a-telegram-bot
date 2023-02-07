import requests
from bs4 import BeautifulSoup as bsoup4
import time
from random import shuffle

user_agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
URL = "https://anekdotovstreet.com/svegie-anekdoty/"



def parser(url):
    responce = requests.get(url,headers=user_agent)
    soup = bsoup4(responce.text, 'lxml')
    jokes = soup.find_all('div', class_='anekdot-text')
    time.sleep(3)
    return [i.text for i in jokes]



list_jokes = parser(URL)
shuffle(list_jokes)
print(list_jokes)

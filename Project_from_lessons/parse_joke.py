from bs4 import BeautifulSoup
import requests
from random import shuffle

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'referer': "https://www.google.com/",
}

url = "https://www.maximonline.ru/entertainment/100-luchshikh-anekdotov-za-desyat-let-2010-2019-id476643/"

req = requests.get(url, headers=headers)


def parse_joke(url, headers):
    r = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(r, "lxml")
    joke = soup.find_all('div',
                          class_="ds-block-text text-style-body-1 ds-article-content__block ds-article-content__block_text")
    return list(filter(lambda x: len(x) > 5,[item.text.strip() for item in joke ]))


jokes= parse_joke(url=url, headers=headers)
shuffle(jokes)


print(F"{len(jokes)} -- количество шуток")


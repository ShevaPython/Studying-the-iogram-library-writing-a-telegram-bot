from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'referer': "https://www.google.com/",
    }


url = "https://kartinkof.club/jumor/smeshnie/2135-smeshnye-kartinki-rossija-52-foto.html"
def parse_photo(url,headers):
    responce = requests.get(url=url, headers=headers)
    src = responce.text
    soup = BeautifulSoup(src,"lxml").find_all(class_="highslide")

    return [item.get('href') for item in soup]


smile = parse_photo(url,headers)

print(F"{len(smile)} - количество фото")
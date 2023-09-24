from bs4 import BeautifulSoup
import requests
url = "https://musicsbaran.ir/various-artists-bravo-hits-120/"

content = requests.get(url).content

soup = BeautifulSoup(content, 'lxml')

all_320 = soup.find_all('a', attrs={'class': "PlayThis"})
# all_320 = soup.find_all('a', href=lambda href:href is not None and href.endswith(".mp3"))
for music in all_320:
    with open('links.txt', 'a') as f:
        f.write(music['data-music'])
        f.write('\n')

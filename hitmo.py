import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4
# pip install lxml

print('Введите название группы на английском(если иностранная группа) или на русском(если группа российская...')
name = input()
url = f'https://rus.hitmotop.com/search?q={name}'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Connactoin': 'keep-alive'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')
heads = block.find_all('div', class_='track__info-r')
print(len(heads))
count = 1
while count <= 48:
    for head in heads:
        w = head.find('a', href=True)
        print(w['href'])
        link = w['href']
        vois = requests.get(link, headers=headers).content
        with open(F'{name}{count}.mp3', 'wb') as f:
            f.write(vois)
        count = count + 1

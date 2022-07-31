from bs4 import BeautifulSoup
import wget
import requests

url = 'https://archive.org/download/MAME_2003-Plus_Reference_Set_2018/roms/'
response = requests.get(url)
content = response.content

lista = []
lista0 = open("not_mature.ini").readlines()
for jogo in lista0:
    jogo = jogo[:-2]
    jogo = jogo+'.zip'
    lista.append(jogo)

site = BeautifulSoup(content, 'html.parser')
games = site.find_all('td')



for game in games:
    gamename = game.find('a')
    try:
        if gamename['href'] in lista:
            lista.remove(gamename['href'])
            print(f'Baixando {gamename["href"]}...')
            wget.download(url + gamename['href'], f'ddownload/{gamename["href"]}')
            print('Ok!')
            print('')

    except:
        pass

texto = open('naobaixados.txt', 'w')
for item in lista:
    texto.write(f'{item}\n')
print('terminou')

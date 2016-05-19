from bs4 import BeautifulSoup
import requests
import os


if __name__ == '__main__':
    url_teste = 'http://legendas.tv/index.php'
    r = requests.get(url_teste)
    soup = BeautifulSoup(r.text, 'lxml')

    for a in soup.find_all('a', href=True):
        print "Found the URL:", a['href']

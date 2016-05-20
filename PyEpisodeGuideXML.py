import urllib2
import csv
import PyTorrentFnc
from bs4 import BeautifulSoup
import requests
              
def DownloadCSV(url):
    url = 'http://www.epguides.com/' + url[3:len(url)]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for content in soup.find_all('pre'):
        f = open('temp.csv', 'w')
        f.write(content.text)
        f.close()
    f = open('temp.csv', 'r')
    lista = []
    for linha in f:
        if len(linha) > 2:
            lista.append(linha)
    f.close()
    PyTorrentFnc.DeletaArquivo('temp.csv')
    f = open('temp.csv', 'w')
    for linha in lista:
        if len(linha) > 2:
            f.write(linha)
    f.close()
    
def ProcuraLinkCSV(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for a in soup.find_all('a', href=True):
        if a['href'].find('CSV') != -1:
            return a['href']
            break

def PreparaXML():
    arquivo_csv = open('temp.csv', 'r')   
    csv_dados = csv.DictReader(arquivo_csv)
    for episodio in csv_dados:
        if episodio['number'][0] != 'S':
            print(episodio['season'], episodio['episode'], episodio['title'])
    arquivo_csv.close()
    #TODO Criar Guia em XML/Show
    
    
if __name__ == '__main__':
    DownloadCSV(ProcuraLinkCSV('http://www.epguides.com/GameofThrones'))
    PreparaXML()
    
    

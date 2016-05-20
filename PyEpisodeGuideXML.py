import csv
import PyTorrentFnc
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from xml.dom import minidom
              
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

def PreparaXML(AsTituloShow):
    doc = minidom.Document()
    show = doc.createElement('show')
    doc.appendChild(show)
    show.setAttribute('titulo', AsTituloShow)
    arquivo_csv = open('temp.csv', 'r')   
    csv_dados = csv.DictReader(arquivo_csv)
    for episodio in csv_dados:
        if episodio['number'][0] != 'S':
            episodio_xml = doc.createElement('episodio')
            titulo = doc.createTextNode(episodio['title'])
            episodio_xml.appendChild(titulo)
            if int(episodio['season']) < 10:
                season = '0' + episodio['season']
            if int(episodio['episode']) < 10:
                episode = '0' + episodio['episode']
            data = datetime.strptime(episodio['airdate'], '%d %b %y')
            episodio_xml.setAttribute('codigo', ('S%sE%s' % (season, episode)))
            episodio_xml.setAttribute('data', data.strftime("%Y-%m-%d"))
            show.appendChild(episodio_xml)
    arquivo_csv.close()
    xml_str = doc.toprettyxml(indent="  ")
    with open(AsTituloShow+".xml", "w") as f:
        f.write(xml_str)
    PyTorrentFnc.DeletaArquivo('temp.csv')
    
if __name__ == '__main__':
    #TODO Preparar Arquivo com lista de seriados
    DownloadCSV(ProcuraLinkCSV('http://www.epguides.com/GameofThrones'))
    PreparaXML('GameOfThrones')
    
    

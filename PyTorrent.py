import urllib2
from PyTorrentFnc import *
from bs4 import BeautifulSoup
import requests

def SeparaArquivos(lista_legendas, lista_download, lista_delete):
    # TO DO: melhorar escolha de arquivos
    for arquivo in lista_legendas:
        if (('HDTV.x264' in arquivo) or ('hdtv-lol' in arquivo)) and not (('720p' in arquivo) or ('1080p' in arquivo)):
                if ('HDTV.x264' in arquivo):
                    posicao_hdtv = arquivo.index('HDTV.x264')
                if ('hdtv-lol' in arquivo):
                    posicao_hdtv = arquivo.index('hdtv-lol')
                lista_download.append(arquivo[0:-4])
        else:
            lista_delete.append(arquivo)

def DeletaArquivo(diretorio, arquivo):
    os.remove(diretorio+'\\'+arquivo+'.srt')

def ProcuraMagnetLink(arquivo):
    url = 'https://kat.cr/usearch/' + arquivo +'/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for a in soup.find_all('a', href=True):
        if a['href'].find('magnet') != -1:
            if (a['href'].find('ettv') != -1) or (a['href'].find('rartv') != -1):
                os.startfile(a['href'])           
   
def Download(lista, diretorio):
    for arquivo in lista:
        print(arquivo)
        try:
            ProcuraMagnetLink(arquivo)
        except:
            print('Erro Magnet Link')
  
if __name__ == '__main__':
    ArquivoIni = LeArquivoIni() 
    dir_legendas = ArquivoIni['dir_legendas']
    dir_falhas = ArquivoIni['dir_falhas']
    lista_legendas = ProcurarArquivos(dir_legendas, '.srt')
    lista_download = []
    lista_delete = []
    SeparaArquivos(lista_legendas, lista_download, lista_delete)
    print('Download:')
    ImprimeLista(lista_download)
    print('Delete:')
    ImprimeLista(lista_delete)
    if len(lista_delete) != 0:
        ImprimeLista(lista_delete)
        mover = raw_input('Mover falhas? ')
        if (mover == 'S') or (mover == 's'):
            print('Deletando')
            MoverArquivosEmLista(dir_legendas, dir_falhas, lista_delete)
    if len(lista_download) != 0:
        print('Iniciando Lista de Download:')
        Download(lista_download, dir_legendas)
        delete = raw_input('Deletar? ')
        if (delete == 'S') or (delete == 's'):
            print('Deletando')
            DeletaLista(dir_falhas, lista_delete)
    raw_input('Fim')

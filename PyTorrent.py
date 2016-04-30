import urllib2
from PyTorrentFnc import *

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

def AbreMagnetLink(magnet_link):
    os.startfile(magnet_link)

def ProcuraMagnetLink(arquivo):
    try:
        try:
            print('Download PirateBay')
            url = "https://thepiratebay.se/search/" + arquivo
            inicio = arquivo + '[ettv]</a>'
            fim = '=' + arquivo
            html = urllib2.urlopen(url).read()
            magnet_link = ExtraiMagnetLink(html, inicio, fim)
            AbreMagnetLink(magnet_link)
        except:
            inicio = "'magnet': '"
            fim = "&dn"
            try:            
                url = "https://kat.cr/usearch/" + arquivo + '%5Bettv%5D/'
                html = urllib2.urlopen(url).read()
                magnet_link = ExtraiMagnetLinkKA(html, inicio, fim)
                AbreMagnetLink(magnet_link)
            except:
                print('Download KickAss Torrents')
                url = "https://kat.cr/usearch/" + arquivo + '%5Brartv%5D/'
                html = urllib2.urlopen(url).read()
                magnet_link = ExtraiMagnetLinkKA(html, inicio, fim)
                AbreMagnetLink(magnet_link)
    except:
        print('Erro no Download')
        #mover legenda para a pasta 'falhas'
        

def ExtraiMagnetLink(html, inicio, fim):
    posicao_inicio = html.find(inicio)
    posicao_fim = html.find(fim)
    html = html[posicao_inicio+len(inicio):posicao_fim+len(fim)]
    posicao_magnet = html.index('magnet')
    html = html[posicao_magnet:]
    return html

def ExtraiMagnetLinkKA(html, inicio, fim):
    posicao_inicio = html.find(inicio)
    posicao_fim = html.find(fim)
    html = html[posicao_inicio+len(inicio):posicao_fim+len(fim)]
    return html

def ImprimeInstrucao(string):
    ImprimeIni = False
    if ImprimeIni:
        print(string)

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
    raw_input('Fim')

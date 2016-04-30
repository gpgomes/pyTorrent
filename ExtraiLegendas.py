import patoolib
import os
from PyTorrentFnc import *

def ProcurarArquivos(diretorio, tipo):
    lista = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(tipo):
                lista.append(file)
    return lista        

def ExtraiArquivo(dir_download, arquivo, dir_legendas):
    patoolib.extract_archive(dir_download+'\\'+arquivo, outdir=dir_legendas)
   
def DeletaArquivo(diretorio, arquivo):
    os.remove(diretorio+'\\'+arquivo)

if __name__ == '__main__':
    ArquivoIni = LeArquivoIni() 
    diretorio = ArquivoIni['diretorio']
    print(diretorio)
    dir_legendas = ArquivoIni['dir_legendas']
    dir_download = ArquivoIni['dir_download']
    lista_rar = ProcurarArquivos(dir_download, '.rar')
    for arquivo_rar in lista_rar:
        if arquivo_rar.find('legenda') != -1:
            #print(arquivo_rar)
            ExtraiArquivo(dir_download, arquivo_rar, dir_legendas)
            DeletaArquivo(dir_download, arquivo_rar)
    DeletaArquivo(dir_legendas, 'Legendas.tv.url')
    raw_input('Fim')    

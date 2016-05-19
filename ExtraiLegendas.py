# Esse script usa o proprio winrar para extrair os arquivos
# verificar se consta no %path%

import os
from PyTorrentFnc import *
import subprocess
from subprocess import call


def ProcurarArquivos(diretorio, tipo):
    lista = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(tipo):
                lista.append(file)
    return lista        

def ExtraiArquivo(dir_download, arquivo, dir_legendas):
    comando = 'unrar x ' + dir_download + arquivo + ' -o+ ' + dir_legendas  + '\\'
    ret = subprocess.call(['cmd', '/c', comando], shell=False)
    if ret != 0:
     if ret < 0:
         print "Killed by signal", -ret
     else:
         print(arquivo + "\n")
         print('Falha, codigo:'+ ret)
    else:
        print "Arquivo Extraido com Sucesso"

def DeletaArquivo(diretorio, arquivo):
    os.remove(diretorio+'\\'+arquivo)

if __name__ == '__main__':
    ArquivoIni = LeArquivoIni() 
    diretorio = ArquivoIni['diretorio']
    dir_legendas = ArquivoIni['dir_legendas']
    dir_download = ArquivoIni['dir_download']
    lista_rar = ProcurarArquivos(dir_download, '.rar')
    for arquivo_rar in lista_rar:
        if arquivo_rar.find('legenda') != -1:
            ExtraiArquivo(dir_download, arquivo_rar, dir_legendas)
            DeletaArquivo(dir_download, arquivo_rar)
    DeletaArquivo(dir_legendas, 'Legendas.tv.url')
    raw_input('Fim')    

import os
import datetime
import time

def LeArquivoIni():
    arquivoIni = 'PyTorrent.ini'
    try:
        with open(arquivoIni) as f:
            linhasIni = f.read().splitlines()
        if len(linhasIni) != 0:
            for linha in linhasIni:
                posicao = linha.find('=')
                tag = linha[0:posicao]
                valorIni = linha[posicao+1:]
                if tag == 'dir':
                    diretorio = valorIni
                elif tag == 'dir_legendas':
                    dir_legendas = valorIni
                elif tag == 'printCMD':
                    printCMD  = valorIni
                elif tag == 'dir_download':
                    dir_download  = valorIni
                elif tag == 'dir_falhas':
                    dir_falhas  = valorIni
            arquivoIni = {'diretorio': diretorio, 'dir_legendas': dir_legendas, 'printCMD': printCMD, 'dir_download': dir_download, 'dir_falhas': dir_falhas}
            return arquivoIni
    except:
        print('Erro ao abrir arquivo .ini')

def ProcurarDiretorios(diretorio):
    lista = []
    for root, dirs, files in os.walk(diretorio):
        for diretorio in dirs:
            lista.append(diretorio)
    return lista

def ProcurarArquivos(diretorio, tipo):
    lista = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(tipo):
                lista.append(file)
    return lista

def ProcurarArquivosMult(diretorio, tipo1, tipo2):
    lista = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(tipo1) or file.endswith(tipo2):
                lista.append(file)
    return lista

def ImprimeLista(lista):
    for dado in lista:
        print(dado)

def ListaEmArquivo(arquivo, lista):
    f = open(arquivo,'w')
    for dado in lista:
        f.write(dado+'\n')
    f.close()

def DeletaLista(diretorio, lista):
    for arquivo in lista:
        os.remove(diretorio+'\\'+arquivo)

def MoverArquivosEmLista(diretorio_inicial, diretorio_final, lista):
    for arquivo in lista:
        os.rename(diretorio_inicial+'\\'+arquivo, diretorio_final+'\\'+arquivo)
        

def LeArquivo(arquivo):
    with open(arquivo) as f:
        lista = f.readlines()
    return lista

def DeletaDiretorio(diretorio):
    os.rmdir(diretorio)

def Log(AsMensagem):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print('%s - %s' % (st, AsMensagem))


        

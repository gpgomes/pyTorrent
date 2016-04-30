from PyTorrentFnc import *

def AcertaArquivo(lista_diretorios, arquivo, diretorio_torrent):
    print(arquivo)
    ettv = False
    rartv = False
    diretorio = arquivo

    if arquivo + '[ettv]' in lista_diretorios:
        ettv = True
        diretorio = diretorio + '[ettv]'
    if arquivo + '[rarbg]' in lista_diretorios:
        rartv = True
        diretorio = diretorio + '[rarbg]'

    arquivo_video = ProcurarArquivosMult(diretorio_torrent + diretorio, '.mp4', '.mkv')
    arquivo_original = diretorio_torrent+'\\'+diretorio+'\\'+arquivo_video[0]
    arquivo_final = diretorio_torrent+'\\'+arquivo+'.mp4'
    MoveArquivoVideo(arquivo_original, arquivo_final)
    #DeletaDiretorio(diretorio_torrent+'\\'+diretorio)
         
def DeletaArquivo(diretorio, arquivo):
    os.remove(diretorio+'\\'+arquivo)

def MoveArquivo(diretorio_inicial, diretorio_final, arquivo):
    os.rename(diretorio_inicial+'\\'+arquivo, diretorio_final+'\\'+arquivo)

def MoveArquivoVideo(arquivo_original, arquivo_final):
    os.rename(arquivo_original, arquivo_final)

def RenomeiaArquivo(arquivo):
    os.rename(diretorio_inicial+'\\'+arquivo, diretorio_final+'\\'+arquivo)
  
if __name__ == '__main__':
    ArquivoIni = LeArquivoIni() 
    diretorio = ArquivoIni['diretorio']
    dir_legendas = ArquivoIni['dir_legendas']
    lista_legendas = ProcurarArquivos(dir_legendas, '.srt')
    lista_diretorios = ProcurarDiretorios(diretorio)
    for legenda in lista_legendas:
        AcertaArquivo(lista_diretorios, legenda[:-4], diretorio)
        MoveArquivo(dir_legendas, diretorio, legenda)
    raw_input('Fim')



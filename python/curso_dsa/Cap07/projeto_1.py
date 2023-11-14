import random

def escolher_palavra():
    try:
        with open(r'Cap07\arquivos\lista_palavras.txt', encoding='utf-8') as texto:
            conteudo = texto.read()
    except FileNotFoundError:
        print('Arquivo não localizado ou não foi possível abrir.')
    else:
        return random.choice(conteudo.split('\n'))

def exibir_forca(erros):
    pass

def exibir_palavra(palavra, letras_corretas):
    pass

def jogo_forca():
    palavra_escolhida = escolher_palavra()
    letras_corretas = []
    letras_incorretas = []
    tentativas_restantes = 6

    while tentativas_restantes > 0:
        exibir_forca(len(letras_incorretas))
        exibir_palavra(palavra_escolhida, letras_corretas)

    if tentativas_restantes == 0:
        print(f'Você perdeu! A palavra era {palavra_escolhida}.')

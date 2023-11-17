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
    if erros == 1:
        print(r'''
    _____
    |   |
    |   O
    |
    |   
    |-----''', end='\n')
    elif erros == 2:
        print(r'''
    _____
    |   |
    |   O
    |   |
    |   
    |-----''', end='\n')
    elif erros == 3:
        print(r'''
    _____
    |   |
    |   O
    |  /|
    |   
    |-----''', end='\n')
    elif erros == 4:
        print(r'''
    _____
    |   |
    |   O
    |  /|\
    |   
    |-----''', end='\n')
    elif erros == 5:
        print(r'''
    _____
    |   |
    |   O
    |  /|\
    |  /
    |-----''', end='\n')
    elif erros == 6:
        print(r'''
    _____
    |   |
    |   O
    |  /|\
    |  / \
    |-----''', end='\n')

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra == ' ':
            print(' ', end=' ')
        elif letra in letras_corretas:
            print(f'{letra}', end=' ')
        else:
            print('_', end=' ')

def jogo_forca():
    palavra_escolhida = escolher_palavra()
    contador = len(palavra_escolhida)
    letras_corretas = []
    letras_incorretas = []
    tentativas_restantes = 6

    while tentativas_restantes > 0:
        exibir_palavra(palavra_escolhida, letras_corretas)
        print(f'\n\nChances restantes: {tentativas_restantes}')
        print(f'Letras erradas: {[letras_incorretas[index] for index, letra in enumerate(letras_incorretas)]}\n')
        if len(letras_corretas) == contador:
            print(f'\nVocê venceu, a palavra é : {palavra_escolhida}')
            break
        
        try:
            tentativa = str(input('Digite uma letra: '))
        except TypeError:
            print('Opção inválida! Tente novamente.')
        
        if tentativa in palavra_escolhida:
            letras_corretas.append(tentativa)
        else:
            letras_incorretas.append(tentativa)
            tentativas_restantes -= 1
            exibir_forca(len(letras_incorretas))
    
    if tentativas_restantes == 0:
        print(f'\n\nVocê perdeu! A palavra era {palavra_escolhida}.')

if __name__ == '__main__':
    print('Bem-vindo(a) ao jogo da forca!\nAdivinhe a palavra abaixo:\n')
    jogo_forca()
    print(f'\nParabéns. Você está aprendendo programação em Python com a DSA.')

# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self) -> None:
          lista_palavras = []
          
          try:
               with open(r'Cap07\arquivos\lista_palavras.txt', 'r', encoding='utf-8') as arquivo:
                    lista_palavras = arquivo.read()
          except FileNotFoundError:
               print('Arquivos não encontrado.')
          
          palavra_sorteada = random.choice(lista_palavras.split('\n'))
          
          print('\nSeja Bem-vindo(a)')
          print(f'{board[0]}\n')
          self.advinhar_letra(palavra_sorteada)

	# Método para adivinhar a letra
     def advinhar_letra(self, palavra):
          letras_tentativas = []
          letras_erradas = []
          fim_jogo = False
          tentativas = 6
          
          while fim_jogo == False:
               self.esconder_letra(palavra)
               print(f'\n\nTentativas restantes: {tentativas}')
               print(f'Letras erradas: {letras_erradas}')
               letra_escolhida = input('Digite uma letra: ')
               if letra_escolhida in letras_tentativas:
                    print('Tente outra letra!')
                    continue
               elif letra_escolhida not in palavra:
                    letras_erradas.append(letra_escolhida)
                    letras_tentativas.append(letra_escolhida)
                    tentativas -= 1
               else:
                    letras_tentativas.append(letra_escolhida)
               
               fim_jogo = self.status_jogo(tentativas, len(letras_erradas))

	# Método para verificar se o jogo terminou
     def acabou_jogo(self, tentativas: int) -> None:
          if tentativas == 0:
               print(f'\nFim do jogo.')
               return True
          else:
               return False
		
	# Método para verificar se o jogador venceu
     def jogador_venceu(self):
          pass
		
	# Método para não mostrar a letra no board
     def esconder_letra(self, texto):
          for letra in texto:
               if letra == ' ':
                    print(' ', end=' ')
               else:
                    print('_', end=' ')
		
	# Método para checar o status do game e imprimir o board na tela
     def status_jogo(self, tentativas, erradas=0):
          fim = self.acabou_jogo(tentativas)
          if fim == True:
               # TODO: verificar se jogador ganhou
               return True
          else:
               print(f'{board[erradas]}\n')
               return False

if __name__ == '__main__':
     jogo = Hangman()
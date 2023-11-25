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
          
          print('Seja Bem-vindo(a)')
          print(f'{board[0]}\n')
          
          palavra = random.choice(lista_palavras.split('\n'))
          self.advinhar_letra(palavra)

	# Método para adivinhar a letra
     def advinhar_letra(self, palavra_sorteada: str):
          tentativas = 6
          letras_erradas = []
          letras_tentativas = []
          letras_unicas = set(palavra_sorteada)
          letras_certas = []
          self.esconder_letra(palavra_sorteada)
          fim_jogo = False

          while fim_jogo == False:
               print(f'\n\nChances restantes: {tentativas}')
               print(f'Letras erradas: {letras_erradas[:]}')
               letra = input('\nDigite uma letra: ')
               if letra not in palavra_sorteada:
                    letras_erradas.append(letra)
                    letras_tentativas.append(letra)
                    tentativas -= 1
               else:
                    letras_tentativas.append(letra)
                    letras_certas.append(letra)
               
               if tentativas != 0:
                    self.status_jogo(palavra_sorteada, letras_certas, len(letras_erradas))
               
               fim_jogo = self.jogador_venceu(letras_unicas, letras_certas)
               fim_jogo = self.acabou_jogo(tentativas, palavra_sorteada)

	# Método para verificar se o jogo terminou
     def acabou_jogo(self, tentativas, palavra):
          if tentativas == 0:
               print(f'\n{board[-1]}\n\nVocê perdeu! A palavra correta é {palavra}.\n')
               return True
          else:
               return False
		
	# Método para verificar se o jogador venceu
     def jogador_venceu(self, conjunto_unico, conjunto_certas):
          if len(conjunto_certas) == len(conjunto_unico):
               print('\nParabéns você venceu!')
               return True
          else:
               return False
		
	# Método para não mostrar a letra no board
     def esconder_letra(self, texto: str) -> None:
          for letra in texto:
               if letra == ' ':
                    print(' ', end=' ')
               else:
                    print('_', end=' ')
		
	# Método para checar o status do game e imprimir o board na tela
     def status_jogo(self, palavra: str, certas: list, tamanho: int) -> None:
          print(f'\n{board[tamanho]}\n')
          for letra in palavra:
               if letra in certas:
                    print(letra, end=' ')
               else:
                    self.esconder_letra(letra)


if __name__ == '__main__':
     jogo = Hangman()
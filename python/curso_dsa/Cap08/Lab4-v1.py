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
          
          palavra = self.esconder_letra(lista_palavras)
          self.advinhar_letra(palavra)

	# Método para adivinhar a letra
     def advinhar_letra(self, palavra_sorteada: str):
          tentativas = 6
          letras_erradas = []
          letras_tentativas = []
          while tentativas > 0:
               print(f'\n\nChances restantes: {tentativas}')
               print(f'Letras erradas: {letras_erradas[:]}')
               letra = input('\nDigite uma letra: ')
               if letra not in palavra_sorteada:
                    letras_erradas.append(letra)
                    tentativas -= 1
	
	# Método para verificar se o jogo terminou
     def acabou_jogo(self):
          pass
		
	# Método para verificar se o jogador venceu
     def jogador_venceu(self):
          pass
		
	# Método para não mostrar a letra no board
     def esconder_letra(self, conteudo: list) -> str:
          """
          Escolhe uma palavra de uma lista de palavras e exibir _ no lugar das letras.

          Args:
              conteudo (list): Coleção de palavras.

          Returns:
              str: Retorna uma palavra escolhida de uma lista. 
          """
          palavra_escolhida = random.choice(conteudo.split('\n'))
          for letra in palavra_escolhida:
               if letra == ' ':
                    print(' ', end=' ')
               else:
                    print('_', end=' ')
          return palavra_escolhida
		
	# Método para checar o status do game e imprimir o board na tela
     def status_jogo(self):
          pass

if __name__ == '__main__':
     jogo = Hangman()
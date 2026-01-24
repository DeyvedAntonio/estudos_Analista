# Exercício 4 — Idade armazenada em lista
#     Crie uma lista contendo nome e idade de uma pessoa.
# 	Informe se a pessoa é maior ou menor de idade.
# 	Exemplo de estrutura:
# 		dados = ["Ana", 17]

#     Objetivo:
#         Trabalhar listas com tipos diferentes.

pessoa = ['Samuel', 29]
resultado = None

if pessoa[-1] > 18:
    resultado = 'Maior de idade'
else:
    resultado = 'Menor de idade'

print(f'{pessoa[0]} tem {pessoa[1]} anos e é {resultado}.')

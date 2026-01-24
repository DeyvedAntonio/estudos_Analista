# Exercício 2 — Comparação de valores
# 	Crie uma lista com dois números.
# 	Compare os dois valores e informe qual é maior ou se são iguais.
# 	Objetivo:
# 		Usar lista + if/else.

lista_numero = [12, 54]

resultado = None
if lista_numero[0] > lista_numero[1]:
    resultado = lista_numero[0]
elif lista_numero[0] < lista_numero[1]:
    resultado = lista_numero[1]
else:
    resultado = 'São iguais'

print(f'O maior é {resultado}')

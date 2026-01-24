# Exercício 3 — Verificação de valor fixo
# 	Crie uma lista com três números.
# 	Verifique se o primeiro número é positivo, negativo ou zero.
# 	Objetivo:
# 		Condicional simples com valor vindo de lista.

lista_numero = [78, 45, 12]
resultado = None

if lista_numero[0] > 0:
    resultado = 'Positivo'
elif lista_numero[0] < 0:
    resultado = 'Negativo'
else:
    resultado = 'Zero'

print(f'O primeiro elemento é {resultado}')

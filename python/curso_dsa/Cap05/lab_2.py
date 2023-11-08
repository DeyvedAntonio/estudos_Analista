# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

def soma(num_1, num_2):
    return num_1 + num_2

def subtracao(num_1, num_2):
    return num_1 - num_2

def multiplicacao(num_1, num_2):
    return num_1 * num_2

def divisao(num_1, num_2):
    return num_1 / num_2

print("\n******************* Calculadora em Python *******************")
print('\nSelecione o número da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')
opcao = int(input('\nDigite sua opção (1/2/3/4): '))
numero_1 = float(input('\nInforme o primeiro número: '))
numero_2 = float(input('\nInforme o segundo número: '))
resultado = None

if opcao == 1:
    resultado = soma(numero_1, numero_2)
elif opcao == 2:
    resultado = subtracao(numero_1, numero_2)
elif opcao == 3:
    resultado = multiplicacao(numero_1, numero_2)
else:
    resultado = divisao(numero_1, numero_2)

print(f'O resultado da operação foi: {resultado}')

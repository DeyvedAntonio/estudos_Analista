# cenário 01
numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

print(numero_1 if numero_1 > numero_2 else numero_2)

# cenário 02
idade = int(input('Digite sua idade: '))

print('Maior de idade' if idade >= 18 else 'Menor de idade')

# cenário 03
valor = int(input('Informe um número: '))
resultado = None

if valor == 0:
    resultado = 'Zero'
elif valor > 0:
    resultado = 'Positivo'
else:
    resultado = 'Negativo'

print(resultado)

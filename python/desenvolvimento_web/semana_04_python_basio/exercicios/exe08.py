conta = {'saldo': -500}

avaliacao = None

if conta['saldo'] > 0:
    avaliacao = 'Positivo'
elif conta['saldo'] < 0:
    avaliacao = 'Negativo'
else:
    avaliacao = 'Zero'

print(f'O saldo da conta é {avaliacao}')

import datetime

hoje = datetime.datetime.now()
print(hoje)

# apenas data
data_hoje = hoje.date()
print(data_hoje)
print(data_hoje.strftime('%d-%m-%Y'))

# ano
ano = hoje.year
print(ano)

# mes
mes = hoje.month
print(mes)

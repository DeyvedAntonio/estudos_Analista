registros = [
    {"nome": "Ana Silva", "idade": 28, "status": "ativo"},
    {"nome": "Bruno Costa", "idade": 34, "status": "inativo"},
    {"nome": "Carla Mendes", "idade": 22, "status": "pendente"},
    {"nome": "Diego Rocha", "idade": 41, "status": "ativo"},
    {"nome": "Elisa Ferreira", "idade": 30, "status": "ativo"},
    {"nome": "Fábio Lima", "idade": 19, "status": "pendente"},
    {"nome": "Gabriela Souza", "idade": 45, "status": "inativo"},
    {"nome": "Henrique Alves", "idade": 27, "status": "ativo"},
    {"nome": "Isabela Nunes", "idade": 36, "status": "ativo"},
    {"nome": "João Pereira", "idade": 52, "status": "inativo"},
    {"nome": "Karina Gomes", "idade": 24, "status": "pendente"},
    {"nome": "Lucas Martins", "idade": 31, "status": "ativo"},
]


def processar_total_registros(lista):
    total_registro = len(lista)
    return total_registro


def processar_total_ativos(lista):
    total_ativos = 0
    for item in lista:
        if item['status'] == 'ativo':
            total_ativos += 1

    return total_ativos


def processar_total_inativos(lista):
    total = 0
    for item in lista:
        if item['status'] == 'inativo':
            total += 1

    return total


print(f'Os dados são: {[registro for registro in registros]}')
print(f'Total de Registros é {processar_total_registros(registros)}')
print(f'Total de ativos é {processar_total_ativos(registros)}')
print(f'Total de inativos é {processar_total_inativos(registros)}')

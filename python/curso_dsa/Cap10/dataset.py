import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Criando dados fictícios para transações financeiras
np.random.seed(42)

# Gerando datas para os últimos 90 dias
data_inicial = datetime.now() - timedelta(days=90)
datas = [data_inicial + timedelta(days=i) for i in range(90)]

# Criando dados para descrição e categoria
descricoes = ['Compra Online', 'Restaurante', 'Supermercado', 'Aluguel', 'Energia', 'Transporte', 'Farmácia']
categorias = ['Compras', 'Alimentação', 'Despesas Fixas', 'Despesas Fixas', 'Contas de Casa', 'Transporte', 'Saúde']

# Gerando valores aleatórios para as transações
valores = np.random.uniform(low=10.0, high=200.0, size=90)

# Criando o DataFrame com os dados
dados_financeiros = pd.DataFrame({
    'Data': datas,
    'Descrição': np.random.choice(descricoes, size=90),
    'Categoria': np.random.choice(categorias, size=90),
    'Valor': valores
})

# Ordenando o DataFrame por data
dados_financeiros = dados_financeiros.sort_values(by='Data').reset_index(drop=True)

# Gravar o dataset
dados_financeiros.to_csv(r'Cap10\arquivos\dados_financeiros.csv')

# Criando dados fictícios
np.random.seed(42)

# Criando dados para alunos
alunos = ['Aluno{}'.format(i) for i in range(1, 11)]

# Criando dados para disciplinas
disciplinas = ['Matematica', 'Portugues', 'Historia', 'Ciencias', 'Ingles']

# Gerando notas aleatórias para cada aluno e disciplina
notas = np.random.randint(60, 100, size=(10, 5))

# Criando o DataFrame com os dados
data = pd.DataFrame(notas, columns=disciplinas, index=alunos)

# Adicionando informações adicionais
data['Sexo'] = ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'F']
data['Idade'] = np.random.randint(15, 18, size=10)

# Visualizando o dataset
data.to_json(r'Cap10\arquivos\dados_escolares.json')

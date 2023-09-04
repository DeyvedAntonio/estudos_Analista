import pandas as pd
import requests
import json

# obter os dados de cada ID usando a API da SDW
url_sdw23 = 'https://sdw-2023-prd.up.railway.app/users/'

def extrair_dados():
    # extrair os dados do arquivo CSV
    dados = pd.read_csv('sdw2023.csv')
    return dados['UserID'].to_list()

def get_user(id):
    resposta = requests.get(f'{url_sdw23}{id}')
    return resposta.json() if resposta.status_code == 200 else None

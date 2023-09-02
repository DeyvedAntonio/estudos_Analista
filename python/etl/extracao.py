import pandas as pd
import requests
import json


# extrair os dados do arquivo CSV
dados = pd.read_csv('sdw2023.csv')
users_id = dados['UserID'].to_list()

# obter os dados de cada ID usando a API da SDW
url_sdw23 = 'https://sdw-2023-prd.up.railway.app/users/'

def get_user(id):
    resposta = requests.get(f'{url_sdw23}{id}')
    return resposta.json() if resposta.status_code == 200 else None

users = [user for id in users_id if (user :=  get_user(id)) is not None]
print(json.dumps(users, indent=2))
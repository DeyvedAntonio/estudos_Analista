import json
import openai
from extracao import get_user, extrair_dados

with open('key_openai.txt', 'r') as key:
    openai_key = key.read()

# extração do ID's dos usuários
users_id = extrair_dados()

# extração dos usuários apartir dos ID's
users = [user for id in users_id if (user :=  get_user(id)) is not None]

def mensagem_openai(user):
    mensagem = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
                {
                    "role": "system", 
                    "content": "Você é especialista em markting digital bancário."
                },
                {
                    "role": "user", 
                    "content": f"Crie mensagens personalizadas para os clientes {user['name']} sobre os benefícios dos investimentos."
                }
            ]
        )
    return mensagem['choices'][0]['message']['content']

for user in users:
    news = mensagem_openai(user)
    print(news)    

print(users['news'])

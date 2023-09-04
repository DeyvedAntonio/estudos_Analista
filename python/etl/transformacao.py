import json
import openai
from extracao import get_user, extrair_dados

openai_key = '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'

# extração do ID's dos usuários
users_id = extrair_dados()

# extração dos usuários apartir dos ID's
users = [user for id in users_id if (user :=  get_user(id)) is not None]

def mensagem_openai():
    mensagem = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
                {
                    "role": "system", 
                    "content": "Você é especialista em markting digital bancário."
                },
                {
                    "role": "user", 
                    "content": f"Crie mensagens personalizadas para os clientes {users['name']} sobre os benefícios dos investimentos."
                }
            ]
        )
    return mensagem['choices'][0]['message']['content']

users['news'].append(mensagem_openai())

print(users['news'])

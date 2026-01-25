status = {'nome': 'Deyved', 'ativo': False}

status_simples = 'Usuário ativo' if status['ativo'] else 'Usuário inativo'

print(f'O status do usuário {status["nome"]} é {status_simples}')

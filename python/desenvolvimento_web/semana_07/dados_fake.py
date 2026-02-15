from random import randint
from brutils import (                                    # type: ignore
    generate_cpf,
    generate_phone,
)
from faker import Faker                                  # type: ignore


def dados_fake(quantidade: int) -> list:
    fake = Faker('pt-BR')
    dados = []
    for id in range(quantidade):
        score = randint(200, 1000)
        renda = float(randint(1500, 10000))
        dados.append(
            {
                'id': id,
                'nome': fake.name(),
                'nascimento': fake.date_of_birth(
                    minimum_age=18, maximum_age=75
                ).strftime("%d-%m-%Y"),
                'cpf': generate_cpf(),
                'telefone': generate_phone("mobile"),
                'score': score,
                'renda': renda,
            }
        )
    return dados

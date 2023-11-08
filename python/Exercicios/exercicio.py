# criar uma lista randômica com 7 elementos, atribuir a uma variável e imprimir essa variável

variavel = list(range(0, 7))
print(variavel)

# funçoes
def soma(num_1: int, num_2: int) -> int:
    """Recebe dois números inteiros e retorna o total.

    Args:
        num_1 (int): primeira parcela da operação de soma.
        num_2 (int): segunda parcela da operação de soma.
    """
    return num_1 + num_2

print(soma(16, 48))


# crie um objeto e seus atributos
class Carro:
    """Classe carro.
    """
    def __init__(self, modelo: str, marca: str, ano: int) -> None:
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def __repr__(self) -> str:
        return f'O carro é do modelo {self.modelo}, da marca {self.marca} e ano {self.ano}.'


meu_carro = Carro('SW4', 'Toyota', 2022)
print(meu_carro)

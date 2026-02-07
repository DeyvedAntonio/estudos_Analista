"""
Módulo contendo a classe Gafanhoto.

Este módulo define a classe Gafanhoto, que representa uma pessoa com nome
e idade e fornece operações simples como incrementar a idade e obter
representações em string e estado para serialização.

Exemplo:
    >>> g = Gafanhoto(nome="Ana", idade=20)
    >>> g.aniversario()
    >>> print(g)
    Ana é Gafanhoto(a) e tem 21 anos de idade.
"""


class Gafanhoto:
    """
    Representa um gafanhoto com nome e idade.

    A classe armazena o nome e a idade do indivíduo e fornece métodos para:
    - incrementar a idade (aniversario);
    - obter uma representação legível (__str__);
    - obter o estado para serialização (__getstate__).

    Attributes:
        nome (str): Nome do gafanhoto.
        idade (int): Idade em anos.
    """

    def __init__(self, nome: str = '', idade: int = 0) -> None:
        """
        Inicializa uma nova instância de Gafanhoto.

        Args:
            nome: Nome do gafanhoto. Valor padrão é string vazia.
            idade: Idade inicial em anos. Valor padrão é 0.
        """
        self.nome = nome
        self.idade = idade

    def aniversario(self) -> None:
        """
        Incrementa a idade do gafanhoto em 1.

        Este método modifica o atributo `idade` da instância.
        """
        self.idade += 1

    def __str__(self) -> str:
        """
        Retorna uma representação legível do objeto.

        A string resultante tem a forma:
            "<Nome> é Gafanhoto(a) e tem <idade> anos de idade."

        Returns:
            Uma string formatada com nome (capitalizado) e idade.
        """
        return f'{self.nome.capitalize()} é Gafanhoto(a) e tem {self.idade} anos de idade.'  # NOQA: E501

    def __getstate__(self) -> object:
        """
        Retorna o estado da instância para fins de serialização.

        O estado retornado é um objeto (neste caso, uma string) que descreve
        os atributos relevantes da instância. Implementações que usam
        pickle ou outra serialização podem preferir retornar um dicionário.

        Returns:
            Um objeto representando o estado atual da instância.
        """
        return {'nome': self.nome, 'idade': self.idade}

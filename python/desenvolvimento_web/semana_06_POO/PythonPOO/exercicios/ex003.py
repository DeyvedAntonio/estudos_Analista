from decimal import Decimal, InvalidOperation


"""
Módulo de exemplo que define a classe ContaBancaria.

Este módulo fornece uma implementação simples de uma conta bancária com
identificador, titular e saldo, além de operações básicas de depósito e saque.
Destina-se a fins didáticos para demonstrar encapsulamento e representação
em string de objetos em Python.
"""


class ContaBancaria:
    """
    Representa uma conta bancária simples.

    A classe armazena o identificador da conta, o nome do titular e o saldo,
    e fornece métodos para depositar, sacar e obter uma representação legível
    da conta.

    Attributes:
        id (str): Identificador único da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo atual da conta em reais.
    """

    def __init__(self, id, nome, saldo: float = 0) -> None:
        """
        Inicializa uma nova instância de ContaBancaria.

        Args:
            id: Identificador da conta (pode ser inteiro ou string).
            nome: Nome do titular da conta.
            saldo: Saldo inicial da conta. Valor padrão é 0.

        Notes:
            O parâmetro `nome` é armazenado no atributo `titular` para deixar
            a API da classe mais expressiva.
        """
        self.id = id
        self.titular = nome
        try:
            self.saldo = Decimal(str(saldo))
        except (InvalidOperation, ValueError):
            "Saldo inválido"

    def __str__(self) -> str:
        """
        Retorna uma representação legível da conta.

        A string tem o formato:
            "A conta {id} de {titular} tem R${saldo:,.2f} de saldo."

        Returns:
            str: Representação formatada com separador de milhares e duas casas decimais.
        """
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def depositar(self, valor: float) -> None:
        """
        Adiciona um valor ao saldo da conta.

        Args:
            valor: Quantia a ser depositada. Deve ser um número não negativo.

        Raises:
            ValueError: Se `valor` for negativo.

        Side effects:
            Modifica o atributo `saldo` da instância.
        """
        try:
            quantia = Decimal(str(valor))
        except (InvalidOperation, ValueError):
            raise ValueError("Valor de depósito inválido")

        if quantia < 0:
            raise ValueError("O valor do depósito não pode ser negativo")

        self.saldo += quantia

    def saque(self, valor: float) -> str:
        """
        Realiza um saque subtraindo o valor do saldo.

        Args:
            valor: Quantia a ser sacada. Deve ser um número não negativo.

        Returns:
            str: Mensagem confirmando o saque com o valor formatado.

        Raises:
            ValueError: Se `valor` for negativo.
            RuntimeError: Se não houver saldo suficiente para o saque.

        Side effects:
            Modifica o atributo `saldo` da instância.
        """
        try:
            quantia = Decimal(str(valor))
        except (InvalidOperation, ValueError):
            raise ValueError("Valor de saque inválido")

        if quantia < 0:
            raise ValueError("O valor do saque não pode ser negativo")

        if quantia > self.saldo:
            raise RuntimeError("Saldo insuficiente")

        self.saldo -= quantia

        return f'Saque de R$ {quantia:,.2f} foi realizado com sucesso!'

class AnaliseCredito:

    def __init__(self, nome_cliente, renda_mensal, valor_solicitado, score_credito, status_analise='Em Análise') -> None:  # NOQA: E501
        self.identificador = f'{renda_mensal}{valor_solicitado}{score_credito}'  # NOQA: E501
        self.nome_cliente = nome_cliente
        self.renda_mensal = renda_mensal
        self.valor_solicitado = valor_solicitado
        self.score_credito = score_credito
        self.status_analise = status_analise

    def mensagem_analise(self, nome_cliente, status):
        return f'Caro, {nome_cliente} sua solicitação foi {status}.'

    def avaliar_risco(self) -> str:

        if self.valor_solicitado > (self.renda_mensal * 0.3):
            self.status_analise = 'Reprovada'
            return self.mensagem_analise(self.nome_cliente, self.status_analise)  # NOQA: E501
        elif self.score_credito <= 600:
            self.status_analise = 'Reprovada'
            return self.mensagem_analise(self.nome_cliente, self.status_analise)  # NOQA: E501
        else:
            self.status_analise = 'Aprovada'
            return self.mensagem_analise(self.nome_cliente, self.status_analise)  # NOQA: E501


if __name__ == '__main__':
    analise_1 = AnaliseCredito('José', 5_000.00, 2_500.00, 800)
    analise_3 = AnaliseCredito('José Maria', 5_000.00, 1_500.00, 800)
    analise_2 = AnaliseCredito('Maria', 7_000.00, 2_500.00, 550)

    print(analise_1.avaliar_risco())
    print(analise_3.avaliar_risco())
    print(analise_2.avaliar_risco())

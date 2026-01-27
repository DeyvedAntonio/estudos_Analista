from datetime import datetime


class AnaliseCredito:

    def __init__(self, nome_cliente, renda_mensal, valor_solicitado, score_credito, status_analise='Em Análise') -> None:    # NOQA: E501
        self.identificador = f'{datetime.now()}{nome_cliente[0:5]}{valor_solicitado}'  # NOQA: E501
        self.nome_cliente = nome_cliente
        self.renda_mensal = renda_mensal
        self.valor_solicitado = valor_solicitado
        self.score_credito = score_credito
        self.status_analise = status_analise

    def avaliar_risco(
            self,
            renda_mensal,
            valor_solicitado,
            score_credito
    ) -> str:

        if valor_solicitado > (renda_mensal * 0.3):
            return 'Reprovado'
        elif score_credito <= 600:
            return 'Reprovado'
        else:
            return 'Aprovado'


if __name__ == '__main__':
    analise_1 = AnaliseCredito('José', 5_000.00, 2_500.00, 800)
    analise_3 = AnaliseCredito('José Maria', 5_000.00, 1_500.00, 800)
    analise_2 = AnaliseCredito('Maria', 7_000.00, 2_500.00, 550)

    print(analise_1.avaliar_risco(5_000.00, 2_500.00, 800))
    print(analise_3.avaliar_risco(5_000.00, 1_500.00, 800))
    print(analise_2.avaliar_risco(7_000.00, 2_500.00, 550))

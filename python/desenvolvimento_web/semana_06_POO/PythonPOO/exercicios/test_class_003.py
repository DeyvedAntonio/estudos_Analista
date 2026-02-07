from ex003 import ContaBancaria


c1 = ContaBancaria(id=112, nome='Deyved', saldo=5_000)
print(c1)
print(c1.depositar(1000))
print(c1.saque(7000))

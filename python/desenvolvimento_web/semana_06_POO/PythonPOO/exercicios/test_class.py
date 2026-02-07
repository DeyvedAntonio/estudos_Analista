from ex002 import Gafanhoto


g1 = Gafanhoto('maria', 17)
print(g1)
g1.aniversario()
print(g1.__dict__)

g2 = Gafanhoto(nome='Mauro', idade=53)
print(g2)
print(g2.__str__)
print(g2.__doc__)

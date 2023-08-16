from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.size = (600, 500)
Window.clearcolor = (233/255, 233/255, 233/255, 1)


usuarios = {}

class Cadastro(BoxLayout):
    """Classe que representar a tela de cadastro."""
    def cadastrar(self):
        nome = self.ids.nome.text
        saldo = self.ids.saldo.text
        if nome in usuarios:
            print(f'Usuário {nome} já cadastrado.')
        else:
            usuarios[nome] = float(saldo)



class Main(App):
    def build(self):
        return Cadastro()


Main().run()
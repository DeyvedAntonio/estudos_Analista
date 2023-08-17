from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import pickle


Window.size = (600, 500)
Window.clearcolor = (233/255, 233/255, 233/255, 1)


try:
    with open('usuarios.pkl', 'rb') as file:
        usuarios = pickle.load(file)
except FileNotFoundError:
    usuarios = {}

class Cadastro(BoxLayout):
    """Classe que representar a tela de cadastro."""
    def cadastrar(self):
        nome = self.ids.nome.text
        saldo = self.ids.saldo.text
        if nome in usuarios:
            self.ids.resposta.text = f'Usuário {nome} já cadastrado.'
        else:
            usuarios[nome] = float(saldo)
            self.ids.resposta.text = f'usuário {nome} cadastrado com sucesso!'


class Main(App):
    def build(self):
        return Cadastro()


Main().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
import pickle


Window.size = (600, 500)
Window.clearcolor = (233/255, 233/255, 233/255, 1)


try:
    with open('usuarios.pkl', 'rb') as file:
        usuarios = pickle.load(file)
except FileNotFoundError:
    usuarios = {}


class Telas(ScreenManager):
    pass


class Usuario(Screen):
    def show(self):
        for name in usuarios:
            self.ids.rel_users.add_widget(Botao(name))


class Botao(Button):
    def __init__(self, nome):
        super().__init__()
        self.text = nome


class Cadastro(Screen):
    """Classe que representar a tela de cadastro."""

    def cadastrar(self):
        nome = self.ids.nome.text
        saldo = self.ids.saldo.text
        if nome in usuarios:
            self.ids.resposta.text = f'Usuário {nome} já cadastrado.'
        elif nome != '':
            if saldo != '':
                usuarios[nome] = float(saldo)
            else:
                usuarios[nome] = 0
            self.ids.resposta.text = f'usuário {nome} cadastrado com sucesso!'
            with open('usuarios.pkl', 'wb') as file:
                pickle.dump(usuarios, file)
            self.ids.nome.text = ''
            self.ids.saldo.text = ''
        else:
            self.ids.resposta.text = 'Insira um nome.'


class Main(App):
    def build(self):
        return Telas()


Main().run()

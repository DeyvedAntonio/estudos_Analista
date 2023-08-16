from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Principal(BoxLayout):
    def mudar_nome(self):
        pass  # TODO


class Exercicio02(App):
    def build(self):
        return Principal()


Exercicio02().run()

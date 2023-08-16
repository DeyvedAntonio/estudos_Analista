from kivy.app import App
from kivy.lang import Builder


class Teste(App):
    def build(self):
        return Builder.load_file('teste.kv')


Teste().run()

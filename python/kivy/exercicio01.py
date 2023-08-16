from kivy.app import App
from kivy.lang import Builder


class Exercicio01(App):
    def build(self):
        return Builder.load_file('exercicio01.kv')


Exercicio01().run()

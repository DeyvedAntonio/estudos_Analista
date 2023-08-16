from kivy.app import App
from kivy.uix.label import Label


class Ola(Label):
    pass


class Test_app(App):
    def build(self):
        return Ola()


Test_app().run()

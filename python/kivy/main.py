from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.size = (600, 500)
Window.clearcolor = (233/255, 233/255, 233/255, 1)


class Cadastro(BoxLayout):
    pass


class Main(App):
    def build(self):
        return Cadastro()


Main().run()
from random import randint
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')
Config.write()


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.numeros_sorteados = None


    def sortear_numeros_da_mega(self) -> int:
        n = []
        numero_sorteado = None
        while True:
            numero_sorteado = randint(1, 60)
            if numero_sorteado not in n:
                n.append(numero_sorteado)
            if len(n) == 6:
                break
        n = sorted(n)
        texto_completo = f'{n[0]} - {n[1]} - {n[2]} - {n[3]} - {n[4]} - {n[5]}'
        return texto_completo
    
    def alterar_label(self):
        self.numeros_sorteados = self.sortear_numeros_da_mega()
        try:
            self.ids.Tela.text = self.numeros_sorteados
        except AttributeError:
            print("Root não encontrado!")


class MainApp(App):
    def build(self):
        return MainLayout()


if __name__=="__main__":
    MainApp().run()
    
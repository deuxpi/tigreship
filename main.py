import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

__version__ = '0.0.1'

class SetupScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SetupScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Player 1 Engine'))
        self.player1 = TextInput(multiline=False)
        self.add_widget(self.player1)
        self.add_widget(Label(text='Player 2 Engine'))
        self.player2 = TextInput(multiline=False)
        self.add_widget(self.player2)


class TigreshipApp(App):
    def build(self):
        return SetupScreen()


if __name__ == '__main__':
    TigreshipApp().run()

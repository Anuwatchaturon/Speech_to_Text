from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class CustomDropDown(BoxLayout):
    pass

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text="ทดสอบ:",font_name="FC Motorway Regular.otf"))
        self.username = TextInput(multiline=False,font_name="FC Motorway Regular.otf")
        self.add_widget(self.username)


class DropApp(App):
    def build(self):
        return CustomDropDown()


if __name__=='__main__':
    DropApp().run()
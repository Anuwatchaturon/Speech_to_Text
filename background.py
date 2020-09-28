import kivy
kivy.require('1.9.0')
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivymd.uix.screen import Screen
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class StartScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
        return StartScreen()

if __name__=='__main__':
    MainApp().run()
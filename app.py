from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
import speech_recognition as sr
#!/usr/bin/env python

# -*- coding: utf-8 -*-
Window.size = (330, 560)

textinput = """
MDTextField:
    id : input
    hint_text: "Enter Text"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width:300
"""

button = """
MDRectangleFlatButton:
        id : button
        text: 'show'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: app.showtext.text = app.input.text 

"""
button2 = """
MDRectangleFlatButton:
        id : button2
        text: 'show2'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: app.show()

"""
showtext = """
MDLabel:
        id : showtext
        text: 'test text '
        halign: 'center'
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
"""
showtext2 = """
MDLabel:
        id : showtext2
        text: ' '
        halign: 'center'
        pos_hint:{'center_x': 0.5, 'center_y': 0.1}
"""
class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Blue"

        self.input = Builder.load_string(textinput)
        screen.add_widget(self.input)

        self.button = Builder.load_string(button)
        screen.add_widget(self.button)

        self.button2 = Builder.load_string(button2)
        screen.add_widget(self.button2)

        self.showtext = Builder.load_string(showtext)
        screen.add_widget(self.showtext)

        self.showtext2 = Builder.load_string(showtext2)
        screen.add_widget(self.showtext2)




        return screen

    def show(self):
       #text = self.input.text
       #print(text)
       self.showtext2.text = self.input.text



MainApp().run()
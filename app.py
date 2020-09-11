from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.window import Window
import speech_recognition as sr
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.menu import MDDropdownMenu, RightContent
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from googletrans import Translator
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem

# -*- coding: utf-8 -*-

Window.size = (330, 560)

language = ['th','en']
font = ['FC Motorway Regular.otf','ABeeZee-Regular.otf']
lanchoose = []
textlist = []
tranlist = []

speechtotext = """
MDLabel:
        id: speechtotext
        text: 'Speech to Text'
        halign: 'center'
        pos_hint:{'center_x': 0.27, 'center_y': 0.93}
        font_style :'Subtitle1'
        font_size : 23

"""
btnrec = """
MDRectangleFlatButton:
        id : btnrec
        text: 'Record'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release: app.checklan()
        readonly: True

"""
btntran = """
MDRectangleFlatButton:
        id : btntran
        text: 'Translate'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 

"""
text = """
MDLabel:
        id: text
        text: 'Your Text '
        theme_text_color: "Custom"
        text_color: 255/255, 195/255, 0/255
        halign: 'center'
        pos_hint:{'center_x': 0.17, 'center_y': 0.85}
        font_style :'Subtitle2'
"""
youtext = """
Label:
        id: youtext
        text: ''
        halign: 'center'
        pos_hint:{'center_x': 0.5, 'center_y': 0.75}
        font_style :'Subtitle2'

"""
trantext = """
MDLabel:
        id: trantext
        text: 'Translater '
        theme_text_color: "Custom"
        text_color: 255/255, 195/255, 0/255
        halign: 'center'
        pos_hint:{'center_x': 0.17, 'center_y': 0.5}
        font_style :'Subtitle2'
"""
youtrantext = """
MDLabel:
        id: youtrantext
        text: ' '
        halign: 'center'
        pos_hint:{'center_x': 0.5, 'center_y': 0.43}
        font_style :'Subtitle2'

"""
btnclear = """
MDRectangleFlatButton:
        id : btnclear
        text: 'Clear'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_release: app.clear()
        readonly: True

"""

lanmenu = '''
<Item>
    ImageLeftWidget:
        source: root.source

FloatLayout:
    MDFlatButton:
        text: "Language"
        pos_hint: {'center_x': .75, 'center_y': .9}
        on_release: app.show_simple_dialog()
'''

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class MainApp(MDApp):
    dialog = None
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"

        self.speechtotext = Builder.load_string(speechtotext)
        screen.add_widget(self.speechtotext)

        self.btnrec = Builder.load_string(btnrec)
        screen.add_widget(self.btnrec)

        self.btntran = Builder.load_string(btntran)
        screen.add_widget(self.btntran)

        self.text = Builder.load_string(text)
        screen.add_widget(self.text)

        # self.youtext = Builder.load_string(youtext)
        # screen.add_widget(self.youtext)

        self.trantext = Builder.load_string(trantext)
        screen.add_widget(self.trantext)

        self.youtrantext = Builder.load_string(youtrantext)
        screen.add_widget(self.youtrantext)

        self.btnclear = Builder.load_string(btnclear)
        screen.add_widget(self.btnclear)

        self.lanmenu = Builder.load_string(lanmenu)
        screen.add_widget(self.lanmenu)

        self.lanin = MDTextField(multiline=False, font_name="FC Motorway Regular.otf")
        self.testthai = Label(text="ท ด ส อ บ ", font_name="FC Motorway Regular.otf",
                              pos_hint={'center_x': 0.85, 'center_y': 0.95})

        self.youtext = Label(text="", font_name="FC Motorway Regular.otf", pos_hint={'center_x': 0.5, 'center_y': 0.75})
        screen.add_widget(self.youtext)

        screen.add_widget(self.lanin)
        screen.add_widget(self.testthai)

        return screen

    def show_simple_dialog(self):

        if not self.dialog:
            self.dialog = MDDialog(
                title="Choose Language",

                buttons=[
                    MDIconButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDIconButton(
                        text="ACCEPT", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()
    def checklan(self):
        if self.lanin in language:
            # find = language.index(lanin)
            #self.Lanin = 'th'

            self.rec()
        else:
            #self.lanin = 'en'

            self.rec()

        pass

    def clear(self):
        self.youtext.text = (" ")

    def rec(self):
        # GUI Blocking Audio Capture
        print("Please say something")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("You have said")
            # audio = r.listen(source)
            word = r.recognize_google(audio, None, self.lanin)
            print(word)
            # textlist.append(word)
            # self.output=(word)
            # self.youtext.text = self.word.text
            self.youtext.text = format(word)

            # self.output=("Audio Recorded Successfully \n ")

        except sr.UnknownValueError:

            self.youtext.text = ("Please Try Again")

        except sr.RequestError as e:

            self.youtext.text = ("Error".format(e))

        pass


if __name__ == '__main__':
    MainApp().run()

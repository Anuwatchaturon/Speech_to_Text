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
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import OneLineAvatarIconListItem

# -*- coding: utf-8 -*-

Window.size = (330, 560)

language = ['th','en']
font = ['FC Motorway Regular.otf','ABeeZee-Regular.otf']
lanchoose = []
textlist = []
tranlist = []

btnrec = """
MDRectangleFlatButton:
        id : btnrec
        text: 'Record'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release: app.rec()
        readonly: True

"""
btntran = """
MDRectangleFlatButton:
        id : btntran
        text: 'Translate'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: app.translator()

"""
youtrantext = """
Label:
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


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"

        self.speechtotext = MDLabel(text= 'Speech to Text',halign= 'center',
                                  pos_hint={'center_x': 0.25, 'center_y': 0.93},font_style ='Subtitle1',font_size = 25)
        screen.add_widget(self.speechtotext)

        self.btnrec = Builder.load_string(btnrec)
        screen.add_widget(self.btnrec)

        self.btntran = Builder.load_string(btntran)
        screen.add_widget(self.btntran)

        self.text = MDLabel(text= 'Your Text ',theme_text_color= "Custom",text_color= (255/255, 195/255, 0/255),
                            halign= 'center',pos_hint={'center_x': 0.17, 'center_y': 0.85},font_style ='Subtitle2')
        screen.add_widget(self.text)

        self.trantext = MDLabel(text= 'Translater ',theme_text_color= "Custom",text_color= (255/255, 195/255, 0/255),
                                halign= 'center',pos_hint={'center_x': 0.17, 'center_y': 0.5},font_style ='Subtitle2')
        screen.add_widget(self.trantext)

        self.youtrantext = Builder.load_string(youtrantext)
        screen.add_widget(self.youtrantext)

        self.btnclear = Builder.load_string(btnclear)
        screen.add_widget(self.btnclear)


        self.testthai = Label(text="ท ด ส อ บ ", font_name="FC Motorway Regular.otf",
                              pos_hint={'center_x': 0.85, 'center_y': 0.95})

        self.youtext = Label(text="fish", font_name="FC Motorway Regular.otf", pos_hint={'center_x': 0.5, 'center_y': 0.75})
        screen.add_widget(self.youtext)

        screen.add_widget(self.testthai)

        return screen
    def checklan(self):

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
            global  word
            word = r.recognize_google(audio, None, 'th')
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
    def translator(self):
            src = 'en'
            dest = 'th'
            translator = Translator()
            testword = 'fish'
            result = translator.translate(testword, src=src, dest=dest)
            self.youtrantext.text = result
        #pass


if __name__ == '__main__':
    MainApp().run()

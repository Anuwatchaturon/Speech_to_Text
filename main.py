from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
import speech_recognition as sr
from kivymd.uix.menu import MDDropdownMenu
from googletrans import Translator

# -*- coding: utf-8 -*-

Window.size = (330, 560)
r = sr.Recognizer()
language = ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da',
            'nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','hi','hmn','hu',
            'is','ig','id','ga','it','ja','jw','kn','kk','km','ku','ky','lo','la','lv','lt','lb','mk','mg','ms'
            'ml','mt','mi','mr','mn','my','ne','no','ps','fa','pl','pt','pa','ro','ru','gd','sr','st','sn','sd',
            'si','sk','sl','so','sm','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','uz','vi','cy','xh',
            'yi','yo','zu','fil','he''ko',]

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
btnrec= """
MDRectangleFlatButton:
        id : btnrec
        text: 'Record'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: app.rec()

"""
btntran= """
MDRectangleFlatButton:
        id : btntran
        text: 'Translate'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 

"""
btnlan= """
MDFillRoundFlatButton:
        id : btnlan
        text: 'Language'
        pos_hint: {'center_x':0.8,'center_y':0.93}
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
MDLabel:
        id: youtext
        text: ''
        halign: 'center'
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
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
class MainApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette="Amber"
        self.theme_cls.theme_style = "Dark"


        self.speechtotext = Builder.load_string(speechtotext)
        screen.add_widget(self.speechtotext)

        self.btnrec = Builder.load_string(btnrec)
        screen.add_widget(self.btnrec)

        self.btntran = Builder.load_string(btntran)
        screen.add_widget(self.btntran)

        self.btnlan = Builder.load_string(btnlan)
        screen.add_widget(self.btnlan)

        self.text = Builder.load_string(text)
        screen.add_widget(self.text)

        self.youtext = Builder.load_string(youtext)
        screen.add_widget(self.youtext)

        self.trantext = Builder.load_string(trantext)
        screen.add_widget(self.trantext)

        self.youtrantext = Builder.load_string(youtrantext)
        screen.add_widget(self.youtrantext)

        return screen
    def checklan(self):
        pass
    def rec(self):
        # GUI Blocking Audio Capture
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            self.output=("You have said")
            word = r.recognize_google(audio)
            #textlist.append(word)
            #self.output=(word)
            self.youtext.text = self.word.text
            #self.output=("Audio Recorded Successfully \n ")
        except Exception as e:
            self.output=("Error ")

        pass


MainApp().run()
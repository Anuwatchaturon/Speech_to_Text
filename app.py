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

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    MDLabel
        id: 'showmlan'
        text: 'xxxx'
        halign: 'center'
        pos_hint: {'center_x':0.85,'center_y':0.94}
    MDFlatButton:
        id : lanchoose
        text: 'Language'
        halign:'center'
        pos_hint: {'center_x':0.15,'center_y':0.2}
        on_press: root.manager.current = 'profile'
    MDFlatButton:
        text: 'Upload'
        halign:'center'
        pos_hint: {'center_x':0.15,'center_y':0.1}
        on_press: root.manager.current = 'upload' 
    Label
        id: speechtotext
        text: 'Speech to Text'
        halign  :'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.93} 
        font_style:'Subtitle1' 
        font_size:25
    MDLabel
        id : text
        text: 'Text' 
        theme_text_color:"Custom"
        text_color:(255 / 255, 195 / 255, 0 / 255)
        halign:'center'
        pos_hint:{'center_x': 0.17, 'center_y': 0.85}
        font_style:'Subtitle2'
    Label
        id : youtext
        text:'test'
        halign:'center' 
        pos_hint:{'center_x': 0.5, 'center_y': 0.78}
    Label
        id: youtrantext
        text: ' '
        halign: 'center'
        pos_hint:{'center_x': 0.5, 'center_y': 0.43}
        font_style :'Subtitle2'
    MDLabel
        id:translator
        text:'Translator '
        theme_text_color:"Custom"
        text_color:(255 / 255, 195 / 255, 0 / 255)
        halign:'center'
        pos_hint:{'center_x': 0.17, 'center_y': 0.5}
        font_style:'Subtitle2'
    MDFlatButton:
        id : btnclear
        text: 'Clear'
        pos_hint: {'center_x':0.83,'center_y':0.20}
        on_press: root.clear()
    MDFlatButton:
        id : btntran
        text: 'Translate'
        pos_hint: {'center_x':0.83,'center_y':0.1}
        on_press: 
    MDRectangleFlatButton:
        id : btnrec
        text: 'Record'
        pos_hint: {'center_x':0.5,'center_y':0.15}
        on_release: root.change()
        readonly: True

<ProfileScreen>:
    name: 'profile'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.2,'center_y':0.9}
        on_press: root.manager.current = 'menu'
        on_press: root.linklan()
        
    MDLabel
        text :' Choose Language'
        halign : 'center'
        pos_hint:{'center_x': 0.7, 'center_y': 0.9} 
        font_style : 'Subtitle1'
        font_size : 20
    MDFlatButton
        id : enbtn
        text: 'English'
        halign:'center'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.enbtn()
    MDFlatButton
        id : thbtn
        text: 'Thai'
        halign:'center'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.thbtn()

    Label
        id : showlan
        text:'xxxx'
        halign:'center' 
        pos_hint:{'center_x': 0.8, 'center_y': 0.95} 


<UploadScreen>:
    name: 'upload'
    MDLabel
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDLabel
        text :' Speech to Text'
        halign : 'center'
        pos_hint:{'center_x': 0.3, 'center_y': 0.93} 
        font_style : 'Subtitle1'
        font_size : 25
"""

class MenuScreen(Screen):
    def change(self):
        txt = 'Cheer boi'
        self.ids.youtext.text = txt

    def clear(self):
        self.ids.youtext.text = ' '
        self.ids.youtrantext.text = ' '

    def linklan(self):
        global x
        self.ids.showmlan.text = x

    pass

class ProfileScreen(Screen):

    def thbtn(self):
        global x
        x = "Thai"
        self.ids.showlan.text = x

    def enbtn(self):
        global x
        x = "English"
        self.ids.showlan.text = x


    pass
class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

class MainApp(MDApp):


    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(screen_helper)


        return screen


    #def clear(self):
        #self.youtext.text = "sdfds "

    def showlan(self):
            showlan.text = "bobob"

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
            word = r.recognize_google(audio, None, self.showlan)
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

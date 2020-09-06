from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from kivy.core.window import Window
import speech_recognition as sr

Window.size = (330, 560)


screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel:
        text:'Speech to Text'
        font_style :'H5'
        theme_text_color: "Custom"
        text_color: 255/255, 255/255, 255/255
        halign: "center"
        pos_hint: {'center_x':0.5,'center_y':0.59}

    MDRectangleFlatButton:
        text: 'START'
        text_color: 255/255, 255/255, 255/255
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'
    
    
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text:'Speech to Text'
        font_style :'Subtitle1'
        halign: 'center'
        pos_hint: {'center_x':0.25,'center_y':0.94}


    MDTextField:
        hint_text: "Language"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        
    
    MDRectangleFlatButton:
        id : lan
        text: 'Start Record'
        text_color: 255/255, 255/255, 255/255
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'
        on_release: self.speech_to_text()
    
"""



class MenuScreen(Screen):

    pass


class ProfileScreen(Screen):
    def speech_to_text(self):
        # while True:
        # lan = str(input('choose language '))
        # lanchoose.append(lan)
        if lan in language:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                self.output("Please say something")
                audio = r.listen(source)
                self.output("Recognizing Now .... ")
                # recognize speech using google
                try:
                    self.output("You have said")
                    word = r.recognize_google(audio, None, lan)
                    textlist.append(word)
                    self.output(word)
                    self.output("Audio Recorded Successfully \n ")
                except Exception as e:
                    self.output("Error ")

    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))

class Speech_to_Text(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "500"
        return screen


Speech_to_Text().run()
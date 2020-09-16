from kivy.lang import Builder

from kivymd.app import MDApp


from kivymd.uix.screen import Screen

from kivymd.uix.button import MDIconButton

KV = '''
Screen:

    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):
    def build(self):
        screen = Screen()
        self.iconbtn = MDIconButton(icon='language-python')
        screen.add_widget(self.iconbtn)
        return screen


Example().run()
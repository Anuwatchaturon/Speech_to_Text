from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
KV = '''
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

class Example(MDApp):
    dialog = None
    def build(self):
        return Builder.load_string(KV)
    def show_simple_dialog(self):

        if not self.dialog:
            self.dialog = MDDialog(
                title="Choose Language",
                type="simple",

                items=[
                    Item(text="English", source="user-1.png"),
                    Item(text="Thai", source="user-2.png"),
                    Item(text="Add account", source="add-icon.png"),
                ],
            )
        self.dialog.open()

Example().run()
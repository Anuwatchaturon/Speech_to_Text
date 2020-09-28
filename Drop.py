from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu

KV = '''
Screen:
    ScrollView:
        do_scroll_x: False
        MDList:
            OneLineAvatarIconListItem:              
                on_size:
                    self.ids._right_container.width = container.width
                    self.ids._right_container.x = container.width
                Container:
                    id: container
                    size_hint_x:None
                    width:dp(288)        
                
                    ListButtonDropdown:
                        id: drop_item
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'Item 0'
                        on_release: self.menu.open()
                            
'''


class Container(IRightBodyTouch, MDBoxLayout):
        adaptive_width = True

class ListButtonDropdown(MDDropDownItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [{"text": f"thai"},{"text": f"english"},{"text": f"abc"}]
        self.menu = MDDropdownMenu(
            caller=self,
            items=menu_items,
            callback=self.set_item2,
            width_mult=4,
        ) 
    def set_item2(self, instance):
        self.set_item(instance.text)  
        self.menu.dismiss()

class Drop(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        
    def build(self):
        return self.screen


Drop().run()
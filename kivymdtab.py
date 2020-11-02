from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

# Builder String
helper_string = '''
ScreenManager:
    Hello:
    
<Hello>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'xDoramming'
        MDTabs:
            id: tabs
            

<Tab>:
    MDLabel:
        id:label
        text:"x" #hello
        halign:"center"
 
<Tab1>:
    MDLabel:
        id:label1
        text:"xDoramming1" #hello
        halign:"left" 
<Tab2>:
    MDCard:
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation:14
        Image:
            source:"cakes.jpg"                         
    '''


class Hello(Screen):
    pass


class Tab(FloatLayout, MDTabsBase):
    pass
class Tab1(FloatLayout, MDTabsBase):
   pass
class Tab2(FloatLayout, MDTabsBase):
   pass
sm = ScreenManager()
sm.add_widget(Hello(name='hello'))


class Switchtabs(MDApp):
    def build(self):
        screen = Screen()

        self .help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        return screen

    def on_start(self):
        self.help_str.get_screen("hello").ids.tabs.add_widget(Tab(text="Cameras"))
        self.help_str.get_screen("hello").ids.tabs.add_widget(Tab1(text="messages"))
        self.help_str.get_screen("hello").ids.tabs.add_widget(Tab2(text="Story"))
Switchtabs().run()

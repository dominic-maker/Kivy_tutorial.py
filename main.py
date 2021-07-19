import kivy
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty

Window.size = (320, 600)


class MusicScreen(Screen):

    def rotate(self):
        pass

    def play(self):
        pass


class SongCover(MDBoxLayout):
    angle = NumericProperty()


class MainApp(MDApp):
    def build(self):
        return MusicScreen()


MainApp().run()

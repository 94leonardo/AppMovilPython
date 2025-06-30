from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import os
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.core.window import Window


class ElementCard(MDCard):
    text = StringProperty()
    sub_text = StringProperty()
    image = StringProperty()


class Ui(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        Builder.load_file("design.kv")  # Asegúrate que el nombre sea correcto
        Window.size = (360, 640)
        return Ui()

    def change_style(self, switch_instance, value):
        self.theme_cls.theme_style = "Dark" if value else "Light"


if __name__ == "__main__":
    MainApp().run()

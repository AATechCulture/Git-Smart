from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from PIL import Image
from pytesseract import pytesseract

#element placement
from kivy.uix.floatlayout import FloatLayout

#import for check boxes and the layout 
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout


from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#imports for checkbox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

#animation for striking line through for checklist
from kivy.animation import Animation

#Change size using size_hint
#Change the color of the button using background_color
#change the color of the border using color
#change position with pos (first number is your x coordinate, the last number is your y coordinate
#bottom left corner is (0,0)
#use bind to make button perform function
class MainScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class TranslateScreen(Screen):
    pass

class ChecklistScreen(Screen):
    pass

class AAApp(MDApp):
    def build(self):
        """screen = Screen()
        self.theme_cls.theme_style = "Dark"
        mapBtn = MDRectangleFlatButton(text = "Map",
                                    pos_hint={"center_x":0.3, "center_y":0.3})
        translateBtn = MDRectangleFlatButton(text = "Translate",
                                    pos_hint={"center_x":0.5, "center_y":0.3})
                                    pos_hint={"center_x":0.5, "center_y":0.3},
                                             on_release=self.translateImg)
        checklistBtn = MDRectangleFlatButton(text = "Checklist",
                                             pos_hint={"center_x":0.7, "center_y":0.3})
        screen.add_widget(mapBtn)
        screen.add_widget(translateBtn)
        screen.add_widget(checklistBtn)
        return screen
        return screen"""
        Builder.load_file("screens_layout.kv.py")
        sm = ScreenManager()

        sm.add_widget(MainScreen(name = "MainScreen"))
        sm.add_widget(TranslateScreen(name = "TranslateScreen"))
        sm.add_widget(ChecklistScreen(name = "ChecklistScreen"))
        sm.add_widget(MapScreen(name = "MapScreen"))

        return sm

if __name__ == '__main__':
    AAApp().run()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.uix.label import Label
from PIL import Image
from pytesseract import pytesseract
from imutils.object_detection import non_max_suppression
from translate import Translator
from kivy.uix.camera import Camera
from kivy.clock import Clock

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
    video_capture = cv2.VideoCapture(0)

class ChecklistScreen(Screen):
    pass

class AAApp(MDApp):
    def build(self):
        Builder.load_file("screens_layout.kv")
        sm = ScreenManager()

        sm.add_widget(MainScreen(name = "MainScreen"))
        sm.add_widget(TranslateScreen(name = "TranslateScreen"))
        sm.add_widget(ChecklistScreen(name = "ChecklistScreen"))

        return sm

if __name__ == '__main__':
    AAApp().run()

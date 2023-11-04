from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

#Change size using size_hint
#Change the color of the button using background_color
#change the color of the border using color
#change position with pos (first number is your x coordinate, the last number is your y coordinate
#bottom left corner is (0,0)
#use bind to make button perform function
class AAApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"

        mapBtn = MDRectangleFlatButton(text = "Map",
                                    pos_hint={"center_x":0.3, "center_y":0.3})
        translateBtn = MDRectangleFlatButton(text = "Translate",
                                    pos_hint={"center_x":0.5, "center_y":0.3})
        checklistBtn = MDRectangleFlatButton(text = "Checklist",
                                             pos_hint={"center_x":0.7, "center_y":0.3})
        screen.add_widget(mapBtn)
        screen.add_widget(translateBtn)
        screen.add_widget(checklistBtn)
        return screen

if __name__ == '__main__':
    AAApp().run()

<MainScreen>:

    MDRectangleFlatButton:
        text: "Map"
        pos_hint:{"center_x":0.3, "center_y":0.3}
        on_release: root.manager.current = "MapScreen"

    MDRectangleFlatButton:
        text: "Translate"
        pos_hint:{"center_x":0.5, "center_y":0.3}
        on_release: root.manager.current = "TranslateScreen"

    MDRectangleFlatButton:
        text: "Checklist"
        on_release: root.manager.current = "ChecklistScreen"
        pos_hint:{"center_x":0.7, "center_y":0.3}

#map screen
<MapScreen>:
    MDRectangleFlatButton:
        text: "Go Back"
        on_release: root.manager.current = "MainScreen"
        #pos_hint: {"center_x": 0,"center_y": 0}

#translate screen
<TranslateScreen>:
    MDRectangleFlatButton:
        text: "Go Back"
        on_release: root.manager.current = "MainScreen"

#checklist screen
<ChecklistScreen>:
    BoxLayout:
        orientation: 'vertical'

        #Label for checklist items
        MDLabel:

            text: 'Checklist'
            size_hint_y: None
            height: '850dp'  # Adjust the height as needed
            text_size: self.width, None  # Set text width to Label width
            halign: 'center'  # Center the text horizontally
            pos_hint: {'center_y': 0.5}  # Center the label vertically
            font_size: '50sp'  # Adjust the font size as needed

            canvas.before:
                Color:
                    rgba: 0.1, 0.5, 0.8, 1  # Black color for the line

                Line:
                    points: self.x, self.y + 100, self.x + self.width, self.y + 100
                    width: 1  # Adjust the line width as needed

                Line:
                    points: self.x, self.y + 400, self.x + self.width, self.y + 400
                    width: 1  # Adjust the line width as needed

                Line:
                    points: self.x, self.y + 200, self.x + self.width, self.y + 200
                    width: 1  # Adjust the line width as needed

                Line:
                    points: self.x, self.y + 300, self.x + self.width, self.y + 300
                    width: 1  # Adjust the line width as needed

                Line:
                    points: self.x, self.y + 250, self.x + self.width, self.y + 250
                    width: 1  # Adjust the line width as needed

                Line:
                    points: self.x, self.y + 350, self.x + self.width, self.y + 350
                    width: 1  # Adjust the line width as needed

                Line:
                    points: self.x, self.y + 150, self.x + self.width, self.y + 150
                    width: 1  # Adjust the line width as needed

        BoxLayout:
            orientation: 'vertical'
            spacing: '5dp'  # Adjust the spacing between checkboxes
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            
            #checkbox #1
            CheckBox:
                size_hint_y: None
                on_active: root.checkbox_selected(self, self.active)  # Define your checkbox handling function
                MDLabel:
                    text: 'Item 1'
                    height: '800dp'  # Adjust the height as needed

            #CheckBox #2
            CheckBox:
                size_hint_y: None
                on_active: root.checkbox_selected(self, self.active)  # Define your checkbox handling function
                MDLabel:
                    text: 'Item 2'
                    height: '700dp'  # Adjust the height as needed

            #CheckBox #3
            CheckBox:
                size_hint_y: None
                on_active: root.checkbox_selected(self, self.active)  # Define your checkbox handling function
                MDLabel:
                    text: 'Item 3'
                    height: '600dp'  # Adjust the height as needed

            #CheckBox #4
            CheckBox:
                size_hint_y: None
                on_active: root.checkbox_selected(self, self.active)  # Define your checkbox handling function
                MDLabel:
                    text: 'Item 4'
                    height: '500dp'  # Adjust the height as needed

            #CheckBox #5
            CheckBox:
                size_hint_y: None
                on_active: root.checkbox_selected(self, self.active)  # Define your checkbox handling function
                MDLabel:
                    text: 'Item 5'
                    height: '400dp'  # Adjust the height as needed

            #CheckBox #6
            CheckBox:
                size_hint_y: None
                on_active: root.checkbox_selected(self, self.active)  # Define your checkbox handling function
                MDLabel:
                    text: 'Item 6'
                    height: '300dp'  # Adjust the height as needed
            
                # add button item to add items to checklist
                Button:
                    size_hint_y: (None)
                    text: 'Add Item'
                    size: ('120dp', '48dp')  # Adjust the size as needed
                    on_press: root.add_checkbox()
                    pos: (root.width - 120, 0)  # Adjust the x-coordinate to move the button to the right

# Go back button on check list screen to go back to the original main screen
        MDRectangleFlatButton:
            text: "Go Back"
            on_release: root.manager.current = "MainScreen"

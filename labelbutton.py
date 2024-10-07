# Importing necessary modules from kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Defining the main application class
class SimpleApp(App):
    def build(self):
        # Creating a layout
        layout = BoxLayout(orientation='vertical')
        
        # Creating a label and adding it to the layout
        self.label = Label(text="Hello, ICT Department")
        layout.add_widget(self.label)
        
        # Creating a button, binding it to the on_button_press function, and adding it to the layout
        button = Button(text="Click Me!")
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)
        
        # Returning the layout to be displayed
        return layout
    
    # Function to handle button click event
    def on_button_press(self, instance):
        self.label.text = "Button Clicked!"

# Running the application
if __name__ == '__main__':
    SimpleApp().run()

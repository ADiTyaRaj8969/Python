import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require('2.1.0')  # Ensure that the Kivy version is 2.1.0 or higher

# Define the main layout class
class TextInputApp(App):

    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a TextInput widget
        self.text_input = TextInput(
            text='Type something here', size_hint=(1, 0.2), multiline=False
        )
        layout.add_widget(self.text_input)

        # Add a Button widget to trigger display of the text
        button = Button(
            text='Display Text', size_hint=(1, 0.2), on_press=self.display_text
        )
        layout.add_widget(button)

        # Add a Label widget to display the text
        self.label = Label(text='Your text will appear here', size_hint=(1, 0.2))
        layout.add_widget(self.label)

        return layout

    # Define the button press event handler
    def display_text(self, instance):
        # Update the label text with the text from the TextInput widget
        self.label.text = self.text_input.text


# Run the app
if __name__ == '__main__':
    TextInputApp().run()

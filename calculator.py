from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Defining the calculator layout and logic
class CalculatorGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(**kwargs)
        self.cols = 4  # Grid layout with 4 columns

        # TextInput field to display the calculation results
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        self.add_widget(self.result)

        # Buttons for numbers and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]

        # Adding buttons to the layout
        for button in buttons:
            self.add_widget(Button(text=button, font_size=24, on_press=self.on_button_press))

        # Clear button to reset the calculator
        self.add_widget(Button(text="C", font_size=24, on_press=self.clear_result))

    # Function to handle button press events
    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text

        # If the equals sign is pressed, evaluate the expression
        if button_text == "=":
            try:
                self.result.text = str(eval(current_text))
            except Exception:
                self.result.text = "Error"
        else:
            # Otherwise, append the pressed button's text to the current expression
            if current_text == "Error":
                self.result.text = button_text  # Reset the result if there's an error
            else:
                self.result.text += button_text

    # Function to clear the result field
    def clear_result(self, instance):
        self.result.text = ""

# Main App class
class CalculatorApp(App):
    def build(self):
        return CalculatorGrid()

# Running the application
if __name__ == '__main__':
    CalculatorApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CounterApp(App):
    def build(self):
        # Main layout
        self.counter = 0  # initialize counter
        layout = BoxLayout(orientation='vertical')

        # Label to display the counter
        self.label = Label(text="Counter: 0", font_size=50)
        layout.add_widget(self.label)

        # Button to increment the counter
        increment_button = Button(text="Increment", font_size=40, size_hint=(1, 0.5))
        increment_button.bind(on_press=self.increment_counter)
        layout.add_widget(increment_button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Counter: {self.counter}"


if __name__ == "__main__":
    CounterApp().run()

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
kivy.require('2.0.0')


class CounterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.counter_label = Label(text="Counter: 0", font_size='40sp')
        self.layout.add_widget(self.counter_label)

        # Button to increment the counter
        self.button = Button(text="Increment Counter", font_size='20sp', size_hint=(1, 0.3))
        self.button.bind(on_press=self.increment_counter)
        self.layout.add_widget(self.button)
        self.counter_value = 0

        return self.layout

    def increment_counter(self, instance):
        self.counter_value += 1
        self.counter_label.text = f"Counter: {self.counter_value}"


if __name__ == "__main__":
    CounterApp().run()

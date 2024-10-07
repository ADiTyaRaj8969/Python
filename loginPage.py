from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginApp(App):
    def build(self):
    
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        

        self.username_label = Label(text="Username:")
        layout.add_widget(self.username_label)
        
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)
        
        self.password_label = Label(text="Password:")
        layout.add_widget(self.password_label)
        
        self.password_input = TextInput(password=True, multiline=False)
        layout.add_widget(self.password_input)
        
        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.check_credentials)
        layout.add_widget(self.login_button)
        
        self.status_label = Label(text="")
        layout.add_widget(self.status_label)
        
        return layout
    
    def check_credentials(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if username == "admin" and password == "password":
            self.status_label.text = "Login Successful"
            self.status_label.color = (0, 1, 0, 1) 
        else:
            self.status_label.text = "Invalid Credentials"
            self.status_label.color = (1, 0, 0, 1) 


if __name__ == '__main__':
    LoginApp().run()

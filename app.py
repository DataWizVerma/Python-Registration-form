import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Header image
        logo_image = Image(source='back.jpg', size_hint=(1, 0.3))  # Replace 'logo.png' with the path to your image
        
        # Adding labels and inputs with improved styling
        name_label = Label(text="Name:", font_size=18, halign="left", valign="middle", size_hint_y=None, height=40)
        name_label.bind(size=name_label.setter('text_size'))
        self.name_input = TextInput(multiline=False, font_size=18, size_hint_y=None, height=40)

        email_label = Label(text="Email:", font_size=18, halign="left", valign="middle", size_hint_y=None, height=40)
        email_label.bind(size=email_label.setter('text_size'))
        self.email_input = TextInput(multiline=False, font_size=18, size_hint_y=None, height=40)

        password_label = Label(text="Password:", font_size=18, halign="left", valign="middle", size_hint_y=None, height=40)
        password_label.bind(size=password_label.setter('text_size'))
        self.password_input = TextInput(multiline=False, font_size=18, password=True, size_hint_y=None, height=40)

        confirm_label = Label(text="Confirm Password:", font_size=18, halign="left", valign="middle", size_hint_y=None, height=40)
        confirm_label.bind(size=confirm_label.setter('text_size'))
        self.confirm_password_input = TextInput(multiline=False, font_size=18, password=True, size_hint_y=None, height=40)

        # Adding a scroll view for better user experience
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 400))
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=20)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        # Adding a register button
        submit_button = Button(text='Register', font_size=18, on_press=self.register, background_color=(0.1, 0.7, 1, 1), size_hint_y=None, height=50)
        
        # Adding elements to the scroll layout
        scroll_layout.add_widget(name_label)
        scroll_layout.add_widget(self.name_input)
        scroll_layout.add_widget(email_label)
        scroll_layout.add_widget(self.email_input)
        scroll_layout.add_widget(password_label)
        scroll_layout.add_widget(self.password_input)
        scroll_layout.add_widget(confirm_label)
        scroll_layout.add_widget(self.confirm_password_input)

        # Adding elements to the main layout
        layout.add_widget(logo_image)
        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)
        layout.add_widget(submit_button)

        return layout

    def register(self, instance):
        # Collect information
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        # Check if all fields are filled
        if not name.strip() or not email.strip() or not password.strip() or not confirm_password.strip():
            message = "Please fill in all fields"
        elif password != confirm_password:
            message = "Passwords do not match"
        else:
            filename = name + '.txt'
            with open(filename, 'w') as file:
                file.write('Name: {}\n'.format(name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
            message = "Registration Successful!\nName: {}\nEmail: {}".format(name, email)

        # Popup
        popup = Popup(title="Registration Status", content=Label(text=message, font_size=18), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    RegistrationApp().run()

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty

class ChatScreen(Screen):
    friend_name = StringProperty('')

    def __init__(self, friend_data=None, is_random=False, user_id=None, **kwargs):
        super().__init__(**kwargs)
        if is_random:
            self.friend_name = f"Random User {user_id}" if user_id else "Random User"
        else:
            self.friend_name = friend_data.get("name", "Unknown") if friend_data else "Unknown"
        self.bind(friend_name=self.update_title)

        Clock.schedule_once(self.set_name, 0.1)

    def set_name(self, *args):
        self.name = 'chat'

    def update_title(self, instance, value):
        self.ids.chat_title.text = value

    def send_message(self):
        message = self.ids.message_input.text
        if message:
            # Add the message to the chat display
            self.ids.chat_display.add_widget(Label(text=f"[Yourself]: {message}", size_hint_y=None, height=40, text_size=(self.width*0.9, None), halign="left"))
            self.ids.message_input.text = ''

            # Placeholder for sending message logic
            print(f"Sending message to {self.friend_name}: {message}")

            # Dummy response after 1 second
            Clock.schedule_once(lambda dt: self.receive_message("Dummy response"), 1)

    def receive_message(self, message):
        # Add the received message to the chat display
        self.ids.chat_display.add_widget(Label(text=f"[{self.friend_name}]: {message}", size_hint_y=None, height=40, text_size=(self.width*0.9, None), halign="left"))

    def go_back(self):
        self.manager.current = 'friends'

    def on_leave(self):
        self.ids.chat_display.clear_widgets()
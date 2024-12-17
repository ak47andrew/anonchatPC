from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.app import App

class FriendItem(BoxLayout):
    name = StringProperty('Test name')
    profile_pic = StringProperty('Test pfp')
    last_message = StringProperty('Test msg')
    def on_release_action(self):
        app = App.get_running_app()
        app.show_chat_screen(friend_data={"name": self.name, "profile_pic": self.profile_pic, "last_message":self.last_message})

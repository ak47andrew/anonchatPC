from kivy.uix.screenmanager import Screen
from components.friend_item import FriendItem
from kivy.app import App
from kivy.uix.scrollview import ScrollView

class FriendsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self, *args):
        self.load_friends()

    def load_friends(self):
        # Example friend data - replace with your actual data
        friends_data = [
            {"name": "Alice", "profile_pic": "alice.png", "last_message": "Hi there!"},
            {"name": "Bob", "profile_pic": "bob.png", "last_message": "How are you?"},
            {"name": "Charlie", "profile_pic": "charlie.png", "last_message": "See you later."},
            {"name": "David", "profile_pic": "david.png", "last_message": "Good morning!"},
            {"name": "Emily", "profile_pic": "emily.png", "last_message": "What's up?"},
            {"name": "Frank", "profile_pic": "frank.png", "last_message": "Long time no see!"},
            {"name": "Grace", "profile_pic": "grace.png", "last_message": "Have a nice day!"},
            {"name": "Henry", "profile_pic": "henry.png", "last_message": "Let's catch up soon."}

        ]
        self.ids.friends_list.clear_widgets()

        for friend in friends_data:
            friend_item = FriendItem(
                name=friend["name"],
                profile_pic=friend["profile_pic"],
                last_message=friend["last_message"]
            )
            friend_item.bind(on_release=lambda instance, friend_data=friend: self.on_friend_selected(friend_data))
            self.ids.friends_list.add_widget(friend_item)

    def on_friend_selected(self, friend_data):
        print(f"Selected friend: {friend_data['name']}")
        # Switch to chat screen
        app = App.get_running_app()
        app.show_chat_screen(friend_data=friend_data)
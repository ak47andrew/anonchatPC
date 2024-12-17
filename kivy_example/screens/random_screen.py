from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from components.loading_spinner import LoadingSpinner  # Import the custom loading spinner
from kivy.app import App

class RandomScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.searching = False
        self.loading_spinner = None  # Initialize to None

    def on_start_search(self):
        self.searching = True
        self.ids.start_button.disabled = True
        self.show_loading()
        # Replace with logic to find a random user
        # After finding a user, call:
        # self.on_user_found(user_id)

    def on_user_found(self, user_id):
        self.searching = False
        self.hide_loading()
        print(f"Found user: {user_id}")

        # Switch to chat screen with the found user
        app = App.get_running_app()
        app.show_chat_screen(user_id=user_id, is_random=True)

    def show_loading(self):
        if not self.loading_spinner:
            self.loading_spinner = LoadingSpinner()
            self.add_widget(self.loading_spinner)

    def hide_loading(self):
        if self.loading_spinner:
            self.remove_widget(self.loading_spinner)
            self.loading_spinner = None
            self.ids.start_button.disabled = False
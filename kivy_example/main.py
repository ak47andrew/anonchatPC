from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.random_screen import RandomScreen
from screens.friends_screen import FriendsScreen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.boxlayout import BoxLayout

class ChatApp(App):
    def build(self):
        # Main layout with TabbedPanel at the bottom
        main_layout = BoxLayout(orientation='vertical')

        # Screen Manager (for switching between Random, Friends, and Chat)
        self.screen_manager = ScreenManager()

        # Initialize screens
        self.random_screen = RandomScreen(name='random')
        self.friends_screen = FriendsScreen(name='friends')

        self.screen_manager.add_widget(self.random_screen)
        self.screen_manager.add_widget(self.friends_screen)

        # Tabbed Panel
        tab_panel = TabbedPanel(do_default_tab=False)

        # Random Tab
        random_tab = TabbedPanelHeader(text='Random')
        random_tab.content = self.random_screen
        tab_panel.add_widget(random_tab)

        # Friends Tab
        friends_tab = TabbedPanelHeader(text='Friends')
        friends_tab.content = self.friends_screen
        tab_panel.add_widget(friends_tab)

        # Add ScreenManager and TabbedPanel to the main layout
        main_layout.add_widget(self.screen_manager)
        main_layout.add_widget(tab_panel)

        return main_layout

    def show_chat_screen(self, friend_data=None, is_random=False, user_id=None):
        # Create and switch to ChatScreen
        from screens.chat_screen import ChatScreen
        chat_screen = ChatScreen(name='chat', friend_data=friend_data, is_random=is_random, user_id=user_id)
        self.screen_manager.add_widget(chat_screen)
        self.screen_manager.current = 'chat'

if __name__ == '__main__':
    ChatApp().run()
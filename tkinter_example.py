import tkinter as tk
from tkinter import ttk, PhotoImage, simpledialog
from tkinter import messagebox
import random
import time
import threading


class ChatApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cross-Platform Chat App")
        self.geometry("600x600")  # Window size
        self.resizable(False, False)

        # Main container for pages
        self.main_container = ttk.Notebook(self)
        self.main_container.pack(expand=1, fill="both")

        # Instantiate pages
        self.random_page = RandomPage(self.main_container)
        self.friends_page = FriendsPage(self.main_container, self.open_friend_chat)

        # Add tabs
        self.main_container.add(self.random_page, text="Random")
        self.main_container.add(self.friends_page, text="Friends")

        # Chat state management
        self.current_friend = None

    def open_friend_chat(self, friend_name):
        """Open chat screen for a specific friend."""
        chat_window = ChatWindow(self, friend_name)
        chat_window.grab_set()  # Modal window


class RandomPage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Layout: Start button, waiting label, and chat area
        self.start_button = ttk.Button(self, text="Start", command=self.find_random_user)
        self.start_button.pack(pady=20)

        self.wait_label = ttk.Label(self, text="", font=("Arial", 12), foreground="blue")
        self.wait_label.pack(pady=10)

        self.chat_area = None  # Placeholder for the chat screen

    def find_random_user(self):
        """Simulate finding a random user."""
        self.start_button.config(state="disabled")
        self.wait_label.config(text="Searching for a random user...")

        # Simulated delay using a thread
        threading.Thread(target=self.simulate_waiting_time).start()

    def simulate_waiting_time(self):
        time.sleep(random.randint(2, 5))  # Simulate delay

        # Update the UI on the main thread
        self.after(0, self.show_chat_screen)

    def show_chat_screen(self):
        """Display a simple chat screen after matching."""
        self.wait_label.config(text="Connected! Start chatting.")
        self.start_button.pack_forget()

        # Chat area
        self.chat_area = ttk.Frame(self)
        self.chat_area.pack(expand=True, fill="both")

        # Placeholder chat text area
        chat_display = tk.Text(self.chat_area, state="disabled", height=20)
        chat_display.pack(pady=10)

        # Input entry
        input_entry = ttk.Entry(self.chat_area)
        input_entry.pack(pady=5)

        # Placeholder buttons
        button_frame = ttk.Frame(self.chat_area)
        button_frame.pack(pady=10)

        for btn_name in ["Send", "Options", "Leave"]:
            ttk.Button(button_frame, text=btn_name, width=10).pack(side="left", padx=5)


class FriendsPage(ttk.Frame):
    def __init__(self, container, open_chat_callback):
        super().__init__(container)

        # Callback for opening a friend's chat
        self.open_chat_callback = open_chat_callback

        # Dummy data for friends
        self.friends_data = [
            {"name": "Alice", "last_msg": "See you soon!", "profile_pic": None},
            {"name": "Bob", "last_msg": "Let's catch up later.", "profile_pic": None},
            {"name": "Charlie", "last_msg": "Did you get my message?", "profile_pic": None},
        ]

        # Scrollable friends list
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Configure canvas and scrollbar
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Populate friends list
        self.populate_friends_list()

    def populate_friends_list(self):
        """Create friend items."""
        for friend in self.friends_data:
            frame = ttk.Frame(self.scrollable_frame, padding=10)
            frame.pack(fill="x", pady=5)

            # Profile picture placeholder
            profile_pic = ttk.Label(frame, text="🧑", font=("Arial", 20))
            profile_pic.pack(side="left", padx=10)

            # Name and last message
            text_frame = ttk.Frame(frame)
            text_frame.pack(side="left", fill="x", expand=True)

            name_label = ttk.Label(text_frame, text=friend["name"], font=("Arial", 12, "bold"))
            name_label.pack(anchor="w")

            last_msg_label = ttk.Label(text_frame, text=friend["last_msg"], font=("Arial", 10))
            last_msg_label.pack(anchor="w")

            # Open chat button
            open_btn = ttk.Button(frame, text="Chat", width=10,
                                  command=lambda n=friend["name"]: self.open_chat_callback(n))
            open_btn.pack(side="right", padx=5)


class ChatWindow(tk.Toplevel):
    """Chat window for a specific friend."""
    def __init__(self, parent, friend_name):
        super().__init__(parent)
        self.title(f"Chat with {friend_name}")
        self.geometry("400x500")
        self.resizable(False, False)

        # Chat display area
        self.chat_display = tk.Text(self, state="disabled", height=20)
        self.chat_display.pack(pady=10)

        # Input entry
        self.input_entry = ttk.Entry(self)
        self.input_entry.pack(pady=5)

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Send", width=10, command=self.send_message).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Close", width=10, command=self.destroy).pack(side="left", padx=5)

    def send_message(self):
        """Handle message sending."""
        msg = self.input_entry.get()
        if msg.strip():
            self.chat_display.config(state="normal")
            self.chat_display.insert("end", f"You: {msg}\n")
            self.chat_display.config(state="disabled")
            self.input_entry.delete(0, "end")


if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
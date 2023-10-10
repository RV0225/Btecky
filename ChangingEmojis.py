import tkinter as tk
import time

class EmojiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Changer")

        self.emojis = [
            "\U0001F604",  # Smiley face
            "\U00002764",  # Heart
            "\U0001F44D",  # Thumbs up
            "\U0001F60D",  # Heart eyes
            "\U0001F609",  # Winking face
        ]

        self.emoji_label = tk.Label(root, text="", font=("Arial", 72))
        self.emoji_label.pack(pady=20)

        self.change_emoji()

    def change_emoji(self):
        for emoji in self.emojis:
            self.emoji_label.config(text=emoji)
            self.root.update()
            time.sleep(2)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmojiApp(root)
    root.mainloop()

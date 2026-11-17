import customtkinter as ctk

class ColonyPickerApp(ctk.CTk):
    def __init__(self):
        # 1. Start up the parent CTk window
        super().__init__()

        # 2. Set the title bar text and starting size (Width x Height)
        self.title("Colony Picker")
        self.geometry("1024x600")
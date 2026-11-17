import customtkinter as ctk


class ColonyPickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PetriPick")
        self.geometry("1024x600")

        # --- 1. CREATE A FRAME (A container box inside the window) ---
        # 'self' means this frame lives directly inside the main window
        self.control_frame = ctk.CTkFrame(self, width=300, corner_radius=10)
        
        # Place the frame on the screen (pady/padx adds empty breathing room around it)
        self.control_frame.pack(pady=40, padx=40, fill="y")

        # --- 2. ADD TEXT (CTkLabel) ---
        # Notice the first argument is 'self.control_frame', NOT 'self'!
        # That puts the text inside the box instead of floating loose in the window.
        self.title_label = ctk.CTkLabel(
            self.control_frame, 
            text="Run Settings", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=(20, 15), padx=30)

        # --- 3. ADD A DROPDOWN (CTkOptionMenu) ---
        self.dish_dropdown = ctk.CTkOptionMenu(
            self.control_frame,
            values=["90mm Petri Dish", "96-Well Plate"],
            command=self.on_dropdown_change  # Function to run when user picks an option
        )
        self.dish_dropdown.pack(pady=10, padx=30)

        # --- 4. ADD A BUTTON (CTkButton) ---
        self.home_button = ctk.CTkButton(
            self.control_frame,
            text="Home Printer",
            height=40,
            command=self.on_button_click  # Function to run when clicked (NO parentheses!)
        )
        self.home_button.pack(pady=20, padx=30)

    # --- FUNCTIONS THAT RUN WHEN YOU INTERACT WITH WIDGETS ---
    def on_dropdown_change(self, selected_choice: str):
        print(f"User selected: {selected_choice}")
        # You can also dynamically change widget text at any time using .configure()
        self.title_label.configure(text=f"Selected: {selected_choice}")

    def on_button_click(self):
        print("Button was clicked! Sending G28 command later...")
        self.home_button.configure(text="Homed!", fg_color="green")
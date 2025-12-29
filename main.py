import customtkinter as ctk
from tkinter import messagebox

# --- Configuration ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class CipherLogic:
    """Separation of Concerns: Logic handles the math."""
    
    @staticmethod
    def process_text(text: str, key: int, mode: str) -> str:
        result = ""
        # Adjust key for decryption
        if mode == "Decrypt":
            key = -key
            
        for char in text:
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
        return result

class CryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("CipherGuard - Encryption Tool")
        self.geometry("1000x650")
        self.minsize(800, 500)
        self.resizable(True, True) 

        # Grid Layout Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) 

        self._create_widgets()

    def _create_widgets(self):
        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 0))
        
        self.lbl_title = ctk.CTkLabel(
            self.header_frame, 
            text="MESSAGE ENCRYPTION SYSTEM", 
            font=("Roboto Medium", 26)
        )
        self.lbl_title.pack()
        
        self.lbl_subtitle = ctk.CTkLabel(
            self.header_frame, 
            text="Secure Caesar Cipher Algorithm", 
            font=("Roboto", 14), 
            text_color="gray70"
        )
        self.lbl_subtitle.pack()

        # --- Main Content Area ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configure Main Frame Grid
        self.main_frame.grid_columnconfigure(0, weight=3)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1) 
        self.main_frame.grid_rowconfigure(3, weight=1) 

        # --- Left Side: Input Text ---
        self.lbl_msg = ctk.CTkLabel(self.main_frame, text="Input Message:", anchor="w", font=("Roboto", 14))
        self.lbl_msg.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.txt_input = ctk.CTkTextbox(self.main_frame, corner_radius=10, font=("Roboto", 14), fg_color="gray20")
        self.txt_input.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        
        self.txt_input.bind("<Enter>", lambda e: self.on_hover(self.txt_input, "enter"))
        self.txt_input.bind("<Leave>", lambda e: self.on_hover(self.txt_input, "leave"))

        # --- Right Side: Settings ---
        self.settings_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        
        # ALIGNMENT FIX: Changed sticky from "ne" to "nw" to pull it closer to the text box
        self.settings_frame.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nw") 

        # Key Entry
        self.lbl_key = ctk.CTkLabel(self.settings_frame, text="Shift Key (Integer):", anchor="w", font=("Roboto", 14))
        self.lbl_key.pack(fill="x", pady=(0, 5))
        
        self.entry_key = ctk.CTkEntry(self.settings_frame, placeholder_text="e.g., 5", font=("Roboto", 14), fg_color="gray20")
        self.entry_key.pack(fill="x", pady=(0, 15))
        
        self.entry_key.bind("<Enter>", lambda e: self.on_hover(self.entry_key, "enter"))
        self.entry_key.bind("<Leave>", lambda e: self.on_hover(self.entry_key, "leave"))

        # Mode Selection
        self.lbl_mode = ctk.CTkLabel(self.settings_frame, text="Operation Mode:", anchor="w", font=("Roboto", 14))
        self.lbl_mode.pack(fill="x", pady=(0, 5))
        
        self.mode_switch = ctk.CTkSegmentedButton(self.settings_frame, values=["Encrypt", "Decrypt"], font=("Roboto", 13))
        self.mode_switch.set("Encrypt")
        self.mode_switch.pack(fill="x", pady=(0, 20))

        # Process Button
        self.btn_process = ctk.CTkButton(
            self.settings_frame, 
            text="PROCESS TEXT", 
            height=45,
            font=("Roboto Medium", 15),
            command=self.perform_cipher
        )
        self.btn_process.pack(fill="x", pady=(10, 0))

        # --- Output Section ---
        self.lbl_result = ctk.CTkLabel(self.main_frame, text="Result:", anchor="w", font=("Roboto", 14))
        self.lbl_result.grid(row=2, column=0, padx=20, pady=(0, 5), sticky="w")

        self.txt_result = ctk.CTkTextbox(self.main_frame, corner_radius=10, fg_color=("gray85", "gray15"), font=("Roboto", 14))
        self.txt_result.grid(row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
        self.txt_result.configure(state="disabled")

        # --- Footer Buttons ---
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.grid(row=2, column=0, padx=20, pady=(0, 20))

        self.btn_clear = ctk.CTkButton(
            self.footer_frame, 
            text="Clear All", 
            fg_color="transparent", 
            border_width=2, 
            text_color=("gray10", "#DCE4EE"),
            height=50,          
            width=160,          
            font=("Roboto Medium", 16), 
            command=self.clear_fields
        )
        self.btn_clear.pack(side="left", padx=15)

        self.btn_copy = ctk.CTkButton(
            self.footer_frame, 
            text="Copy Result", 
            fg_color="#2CC985", 
            hover_color="#229e68",
            height=50,          
            width=160,          
            font=("Roboto Medium", 16), 
            command=self.copy_to_clipboard
        )
        self.btn_copy.pack(side="left", padx=15)

    def on_hover(self, widget, event_type):
        """Changes the background color of the widget on hover."""
        if event_type == "enter":
            widget.configure(fg_color="gray30") 
        elif event_type == "leave":
            widget.configure(fg_color="gray20") 

    def perform_cipher(self):
        msg = self.txt_input.get("1.0", "end-1c")
        key_str = self.entry_key.get()
        mode = self.mode_switch.get()

        if not msg.strip():
            messagebox.showwarning("Input Error", "Please enter a message to process.")
            return

        try:
            key = int(key_str)
        except ValueError:
            messagebox.showerror("Input Error", "Key must be an integer.")
            return

        result = CipherLogic.process_text(msg, key, mode)
        
        self.txt_result.configure(state="normal")
        self.txt_result.delete("1.0", "end")
        self.txt_result.insert("1.0", result)
        self.txt_result.configure(state="disabled")

    def clear_fields(self):
        self.txt_input.delete("1.0", "end")
        self.entry_key.delete(0, "end")
        self.txt_result.configure(state="normal")
        self.txt_result.delete("1.0", "end")
        self.txt_result.configure(state="disabled")

    def copy_to_clipboard(self):
        result = self.txt_result.get("1.0", "end-1c")
        if result and result.strip():
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update() 
            messagebox.showinfo("Success", "Result copied to clipboard!")
        else:
             messagebox.showwarning("Warning", "No result to copy!")

if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()

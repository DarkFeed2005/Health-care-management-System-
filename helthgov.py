import customtkinter as ctk
import tkinter as tk
import webview  # To embed the website inside the app
import subprocess  # To open other Python files

# Initialize app
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MOH Healthcare System - Sri Lanka")
        self.geometry("1000x680+325+175")

        # Header Frame (Navigation Bar)
        self.header_frame = ctk.CTkFrame(self, height=60, fg_color="#2B2B2B", corner_radius=0)
        self.header_frame.pack(fill="x")

        # Navigation Buttons
        self.home_btn = ctk.CTkButton(self.header_frame, text="🏠 Home", command=lambda: self.open_web("https://www.health.gov.lk"), width=120)
        self.home_btn.pack(side="left", padx=20, pady=10)

        self.about_btn = ctk.CTkButton(self.header_frame, text="ℹ️ About", command=lambda: self.open_web("https://www.health.gov.lk/about"), width=120)
        self.about_btn.pack(side="left", padx=20, pady=10)

        self.services_btn = ctk.CTkButton(self.header_frame, text="🩺 Services", command=lambda: self.open_web("https://www.health.gov.lk/services"), width=120)
        self.services_btn.pack(side="left", padx=20, pady=10)

        self.contact_btn = ctk.CTkButton(self.header_frame, text="📞 Contact Us", command=lambda: self.open_web("https://www.health.gov.lk/contact"), width=120)
        self.contact_btn.pack(side="left", padx=20, pady=10)

        self.signin_btn = ctk.CTkButton(self.header_frame, text="🔑 Sign In", command=self.open_signin, fg_color="#0084FF", width=120)
        self.signin_btn.pack(side="right", padx=20, pady=10)

        # **Toggle Button for Dark/Light Mode**
        self.toggle_mode_btn = ctk.CTkButton(self.header_frame, text="🌗 Toggle Mode", command=self.toggle_mode, width=120)
        self.toggle_mode_btn.pack(side="right", padx=20, pady=10)

        # Embedded Web Viewer
        self.web_view = webview.create_window("MOH Healthcare System", "https://www.health.gov.lk")
        webview.start()

    def open_web(self, url):
        """Open the selected webpage inside the app"""
        self.web_view.load_url(url)

    def open_signin(self):
        """Open Login Window (`login.py`)"""
        subprocess.run(["python", "login.py"])  # Opens login.py

    def toggle_mode(self):
        """Switch between Dark and Light mode dynamically"""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        tk.messagebox.showinfo("Theme Changed", f"Switched to {new_mode} Mode")

# Run the app
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
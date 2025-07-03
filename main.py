#main
import sys
print(sys.executable)
import customtkinter as ctk
import tkinter as tk
import webview  
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
        self.home_btn = ctk.CTkButton(self.header_frame, text="🏠 Home", command=self.show_home, width=120)
        self.home_btn.pack(side="left", padx=20, pady=10)

        self.about_btn = ctk.CTkButton(self.header_frame, text="ℹ️ About", command=self.show_about, width=120)
        self.about_btn.pack(side="left", padx=20, pady=10)

        self.services_btn = ctk.CTkButton(self.header_frame, text="🩺 Services", command=self.show_services, width=120)
        self.services_btn.pack(side="left", padx=20, pady=10)

        self.contact_btn = ctk.CTkButton(self.header_frame, text="📞 Contact Us", command=self.show_contact, width=120)
        self.contact_btn.pack(side="left", padx=20, pady=10)

        self.signin_btn = ctk.CTkButton(self.header_frame, text="🔑 Sign In", command=self.open_signin, fg_color="#0084FF", width=120)
        self.signin_btn.pack(side="right", padx=20, pady=10)

        # Toggle Button for Dark/Light Mode
        self.toggle_mode_btn = ctk.CTkButton(self.header_frame, text="🌗 Toggle Mode", command=self.toggle_mode, width=120)
        self.toggle_mode_btn.pack(side="right", padx=20, pady=10)

        # Main content frame (Webview embedded in Home section)
        self.content_frame = ctk.CTkFrame(self, corner_radius=10)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_home()  # Load Home Page by default

    def clear_content(self):
        """Clear previous content before updating"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        """Display Home Page with Embedded Webview"""
        self.clear_content()

        # Welcome Text
        ctk.CTkLabel(self.content_frame, text="🏥 Welcome to MOH Healthcare System!", font=("Arial", 24)).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="Providing trusted medical care and services for the community.", font=("Arial", 16)).pack(pady=5)

        # **Embed Webview Inside Home Section**
        webview.create_window("MOH Healthcare System", "https://www.health.gov.lk", frameless=True)
        webview.start()

    def show_about(self):
        """Display About Page Content"""
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="ℹ️ About MOH Healthcare System", font=("Arial", 24)).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="We offer top-tier medical services, patient support, and healthcare technology solutions.", font=("Arial", 16)).pack(pady=5)

    def show_services(self):
        """Display Services Page Content"""
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="🩺 Our Medical Services", font=("Arial", 24)).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="We provide expert consultation, emergency care, and medical treatments tailored to your needs.", font=("Arial", 16)).pack(pady=5)

    def show_contact(self):
        """Display Contact Us Page Content"""
        self.clear_content()
        ctk.CTkLabel(self.content_frame, text="📞 Contact MOH Healthcare System", font=("Arial", 24)).pack(pady=10)
        ctk.CTkLabel(self.content_frame, text="📍 Address: 123 Health Street, City\n📞 Phone: +1-234-567-890\n✉️ Email: support@mohhealthcare.com", font=("Arial", 16)).pack(pady=5)

    def open_signin(self):
        """Open Login Window (`login.py`)"""
        subprocess.run(["python", "login.py"])  # Opens login.py

    def toggle_mode(self):
        """Switch between Dark and Light mode dynamically"""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        

# Run the app
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import subprocess  # To reopen login.py after logout

# Initialize app
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

class UserDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MOH Healthcare - User Dashboard")
        self.geometry("900x550")
        self.sidebar_visible = True

        # Sidebar Frame
        self.sidebar = ctk.CTkFrame(self, width=220, height=550, corner_radius=0, fg_color="#2B2B2B")
        self.sidebar.place(x=0, y=0)

        # Sidebar Buttons
        self.toggle_sidebar_btn = ctk.CTkButton(self.sidebar, text="⇦ Hide Sidebar", command=self.toggle_sidebar, width=180,)
        self.toggle_sidebar_btn.pack(pady=15)

        self.profile_btn = ctk.CTkButton(self.sidebar, text="👤 Profile", command=lambda: self.update_content("Profile"), width=180)
        self.profile_btn.pack(pady=10)
        
        self.appointments_btn = ctk.CTkButton(self.sidebar, text="📅 Appointments", command=lambda: self.update_content("Appointments"), width=180)
        self.appointments_btn.pack(pady=10)
        
        self.records_btn = ctk.CTkButton(self.sidebar, text="📜 Medical Records", command=lambda: self.update_content("Medical Records"), width=180)
        self.records_btn.pack(pady=10)
        
        self.billing_btn = ctk.CTkButton(self.sidebar, text="💳 Billing", command=lambda: self.update_content("Billing"), width=180)
        self.billing_btn.pack(pady=10)

        self.help_btn = ctk.CTkButton(self.sidebar, text="❓ Help & Support", command=lambda: self.update_content("Help & Support"), width=180)
        self.help_btn.pack(pady=10)

        # Dark/Light Mode Toggle Button
        self.toggle_mode_btn = ctk.CTkButton(self.sidebar, text="🌗 Toggle Mode", command=self.toggle_mode, width=180)
        self.toggle_mode_btn.pack(pady=20)

        # Logout Button with Confirmation
        self.logout_btn = ctk.CTkButton(self.sidebar, text="🚪 Log Out", command=self.logout, width=180, fg_color="#FF6B6B", hover_color="#FF9999")
        self.logout_btn.pack(side="bottom", pady=20)

        # Floating "Show Sidebar" Button (Initially Hidden)
        self.show_sidebar_btn = ctk.CTkButton(self, text="⇨ Show Sidebar", command=self.toggle_sidebar, width=120)
        self.show_sidebar_btn.place(x=-150, y=20)  # Hidden initially

        # Main content frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, width=680, height=550)
        self.main_frame.place(x=230, y=0)

        self.label = ctk.CTkLabel(self.main_frame, text="Welcome to Your Dashboard!", font=("Arial", 20))
        self.label.pack(pady=600)
        
        

   

    def update_content(self, section):
        """Update main content dynamically"""
        self.label.configure(text=f"{section} Section")

    def toggle_sidebar(self):
        """Animate Sidebar Hide/Show Effect"""
        if self.sidebar_visible:
            for x in range(0, -220, -10):  # Slide sidebar left
                self.sidebar.place(x=x, y=0)
                self.update()
            self.toggle_sidebar_btn.configure(text="⇨ Show Sidebar")
            self.show_sidebar_btn.place(x=10, y=20)  # Show floating button
        else:
            for x in range(-220, 0, 10):  # Slide sidebar right
                self.sidebar.place(x=x, y=0)
                self.update()
            self.toggle_sidebar_btn.configure(text="⇦ Hide Sidebar")
            self.show_sidebar_btn.place(x=-150, y=20)  # Hide floating button

        self.sidebar_visible = not self.sidebar_visible  # Toggle state

    def toggle_mode(self):
        """Switch between Dark and Light mode dynamically"""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        

    def logout(self):
        """Display logout confirmation & redirect to login"""
        if messagebox.askyesno("Logout", "Are you sure you want to log out?"):
            self.destroy()  # Close the dashboard
            subprocess.run(["python", "login.py"])  # Open the login page

# Run the app
if __name__ == "__main__":
    app = UserDashboard()
    app.mainloop()
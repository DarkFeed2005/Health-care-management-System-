import customtkinter as ctk
import tkinter as tk

# Initialize app
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

class AdvancedHealthcareDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MOH Healthcare Management System")
        self.geometry("900x550")
        self.sidebar_visible = True

        # Sidebar Frame
        self.sidebar = ctk.CTkFrame(self, width=220, height=550, corner_radius=0, fg_color="#2B2B2B")
        self.sidebar.place(x=0, y=0)

        # Sidebar Buttons
        self.toggle_sidebar_btn = ctk.CTkButton(self.sidebar, text="⇦ Hide Sidebar", command=self.toggle_sidebar, width=180)
        self.toggle_sidebar_btn.pack(pady=15)

        self.home_btn = ctk.CTkButton(self.sidebar, text="🏠 Home", command=lambda: self.update_content("Home"), width=180)
        self.home_btn.pack(pady=10)
        
        self.patients_btn = ctk.CTkButton(self.sidebar, text="👩‍⚕️ Patients", command=lambda: self.update_content("Patients"), width=180)
        self.patients_btn.pack(pady=10)
        
        self.appointments_btn = ctk.CTkButton(self.sidebar, text="📅 Appointments", command=lambda: self.update_content("Appointments"), width=180)
        self.appointments_btn.pack(pady=10)
        
        self.billing_btn = ctk.CTkButton(self.sidebar, text="💳 Billing", command=lambda: self.update_content("Billing"), width=180)
        self.billing_btn.pack(pady=10)

        # Dark Mode Toggle
        self.toggle_mode = ctk.CTkButton(self.sidebar, text="🌗 Toggle Mode", command=self.toggle_mode, width=180)
        self.toggle_mode.pack(pady=20)

        # Main content frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, width=680, height=550)
        self.main_frame.place(x=230, y=0)

        self.label = ctk.CTkLabel(self.main_frame, text="Welcome to the Dashboard!", font=("Arial", 20))
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
        else:
            for x in range(-220, 0, 10):  # Slide sidebar right
                self.sidebar.place(x=x, y=0)
                self.update()
            self.toggle_sidebar_btn.configure(text="⇦ Hide Sidebar")

        self.sidebar_visible = not self.sidebar_visible  # Toggle state

    def toggle_mode(self):
        """Switch between Dark and Light mode dynamically"""
        current_mode = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Light" if current_mode == "Dark" else "Dark")

# Run the app
if __name__ == "__main__":
    app = AdvancedHealthcareDashboard()
    app.mainloop()
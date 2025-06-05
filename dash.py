import customtkinter as ctk

# Initialize app
ctk.set_appearance_mode("Dark")  # Options: "Dark" or "Light"
ctk.set_default_color_theme("blue")

class HealthcareDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("MOH Healthcare Management System")
        self.geometry("800x500")

        # Sidebar frame
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        # Sidebar buttons
        self.home_btn = ctk.CTkButton(self.sidebar, text="🏠 Home", command=lambda: self.update_content("Home"))
        self.home_btn.pack(pady=10)
        
        self.patients_btn = ctk.CTkButton(self.sidebar, text="👩‍⚕️ Patients", command=lambda: self.update_content("Patients"))
        self.patients_btn.pack(pady=10)
        
        self.appointments_btn = ctk.CTkButton(self.sidebar, text="📅 Appointments", command=lambda: self.update_content("Appointments"))
        self.appointments_btn.pack(pady=10)
        
        self.billing_btn = ctk.CTkButton(self.sidebar, text="💳 Billing", command=lambda: self.update_content("Billing"))
        self.billing_btn.pack(pady=10)

        # Dark mode toggle
        self.toggle_mode = ctk.CTkButton(self.sidebar, text="🌗 Toggle Mode", command=self.toggle_mode)
        self.toggle_mode.pack(pady=20)

        # Main content area
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.label = ctk.CTkLabel(self.main_frame, text="Welcome to the Dashboard!", font=("Arial", 18))
        self.label.pack(pady=20)

    def update_content(self, section):
        """Update main display based on sidebar selection"""
        self.label.configure(text=f"{section} Section")

    def toggle_mode(self):
        """Toggle between Dark and Light mode"""
        current_mode = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Light" if current_mode == "Dark" else "Dark")

# Run the app
if __name__ == "__main__":
    app = HealthcareDashboard()
    app.mainloop()
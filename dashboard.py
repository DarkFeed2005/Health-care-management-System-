import customtkinter as ctk
import matplotlib.pyplot as plt

# Initialize main app
ctk.set_appearance_mode("Dark")  #  "Dark" or "Light"
ctk.set_default_color_theme("blue")  #  change the theme color

class HealthcareDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("MOH Healthcare Management System")
        self.geometry("1000x680+325+175")

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.sidebar_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Sidebar buttons
        self.home_btn = ctk.CTkButton(self.sidebar_frame, text="🏠 Home", command=self.show_home)
        self.home_btn.pack(pady=10)
        self.patients_btn = ctk.CTkButton(self.sidebar_frame, text="👩‍⚕️ Patients", command=self.show_patients)
        self.patients_btn.pack(pady=10)
        self.appointments_btn = ctk.CTkButton(self.sidebar_frame, text="📅 Appointments", command=self.show_appointments)
        self.appointments_btn.pack(pady=10)
        self.billing_btn = ctk.CTkButton(self.sidebar_frame, text="💳 Billing", command=self.show_billing)
        self.billing_btn.pack(pady=10)

        # Dark/Light mode toggle
        self.toggle_mode = ctk.CTkButton(self.sidebar_frame, text="🌗 Toggle Mode", command=self.toggle_mode)
        self.toggle_mode.pack(pady=20)

        # Main display area
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.label = ctk.CTkLabel(self.main_frame, text="Welcome to MOH Healthcare Dashboard", font=("Arial", 18))
        self.label.pack(pady=20)

    def show_home(self):
        self.label.configure(text="🏠 Home Dashboard")

    def show_patients(self):
        self.label.configure(text="👩‍⚕️ Patient Management")

    def show_appointments(self):
        self.label.configure(text="📅 Appointment Scheduling")

    def show_billing(self):
        self.label.configure(text="💳 Billing System")

    def toggle_mode(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        
    
# Run the app
if __name__ == "__main__":
    app = HealthcareDashboard()
    app.mainloop()
    
    

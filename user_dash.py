import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess  # To reopen signup.py after logout
import mysql.connector  # MySQL database connection

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="****", database="moh_healthcare")
cursor = conn.cursor()

# Initialize app
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

class UserDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MOH Healthcare - User Dashboard")
        self.geometry("900x550")
        self.sidebar_visible = True

        # **Define user attributes before fetching data**
        self.user_name = "Unknown User"
        self.user_email = "hello@example.com"  # Replace with logged-in user's email

        # Fetch user details from the database
        self.fetch_user_data()

        # Sidebar Frame
        self.sidebar = ctk.CTkFrame(self, width=220, height=550, corner_radius=0, fg_color="#2B2B2B")
        self.sidebar.place(x=0, y=0)

        # Sidebar Buttons
        self.toggle_sidebar_btn = ctk.CTkButton(self.sidebar, text="⇦ Hide Sidebar", command=self.toggle_sidebar, width=180)
        self.toggle_sidebar_btn.pack(pady=15)

        self.profile_btn = ctk.CTkButton(self.sidebar, text="👤 Profile", command=self.show_profile, width=180)
        self.profile_btn.pack(pady=10)
        
        self.appointments_btn = ctk.CTkButton(self.sidebar, text="📅 Appointments", command=self.show_appointments, width=180)
        self.appointments_btn.pack(pady=10)
        
        self.records_btn = ctk.CTkButton(self.sidebar, text="📜 Medical Records", command=self.show_medical_records, width=180)
        self.records_btn.pack(pady=10)
        
        self.billing_btn = ctk.CTkButton(self.sidebar, text="💳 Billing", command=self.show_billing, width=180)
        self.billing_btn.pack(pady=10)

        self.help_btn = ctk.CTkButton(self.sidebar, text="❓ Help & Support", command=self.show_help_support, width=180)
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

    def fetch_user_data(self):
        """Fetch user details from the database"""
        cursor.execute("SELECT name, email FROM users WHERE email=%s", (self.user_email,))
        result = cursor.fetchone()
        if result:
            self.user_name, self.user_email = result
        else:
            messagebox.showerror("Error", "User not found in database!")

    def clear_main_frame(self):
        """Clear previous content before updating"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_profile(self):
        """Display user profile details"""
        self.clear_main_frame()
        self.fetch_user_data()  # Ensure updated details are displayed

        # Display Profile Information
        ctk.CTkLabel(self.main_frame, text="👤 User Profile", font=("Arial", 20)).pack(pady=10)
        ctk.CTkLabel(self.main_frame, text=f"Name: {self.user_name}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(self.main_frame, text=f"Email: {self.user_email}", font=("Arial", 16)).pack(pady=5)
        
        ctk.CTkButton(self.main_frame, text="Change Profile", command=self.change_profile, fg_color="#0084FF").pack(pady=10)

    def show_appointments(self):
        """Display upcoming appointments"""
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="📅 Your Appointments", font=("Arial", 20)).pack(pady=10)

    def show_medical_records(self):
        """Display medical history"""
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="📜 Medical Records", font=("Arial", 20)).pack(pady=10)

    def show_billing(self):
        """Display billing details"""
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="💳 Billing Information", font=("Arial", 20)).pack(pady=10)

    def show_help_support(self):
        """Display help & support options"""
        self.clear_main_frame()
        ctk.CTkLabel(self.main_frame, text="❓ Help & Support", font=("Arial", 20)).pack(pady=10)

    def toggle_sidebar(self):
        """Animate Sidebar Hide/Show Effect"""
        if self.sidebar_visible:
            self.sidebar.place_forget()
            self.show_sidebar_btn.place(x=10, y=20)  # Show floating button
        else:
            self.sidebar.place(x=0, y=0)
            self.show_sidebar_btn.place(x=-150, y=20)  # Hide floating button

        self.sidebar_visible = not self.sidebar_visible  # Toggle state

    def toggle_mode(self):
        """Switch between Dark and Light mode dynamically"""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        messagebox.showinfo("Theme Changed", f"Switched to {new_mode} Mode")

    def logout(self):
        """Display logout confirmation & redirect to signup"""
        if messagebox.askyesno("Logout", "Are you sure you want to log out?"):
            self.destroy()  # Close the dashboard
            subprocess.run(["python", "signup.py"])  # Open the signup page

# Run the app
if __name__ == "__main__":
    app = UserDashboard()
    app.mainloop()
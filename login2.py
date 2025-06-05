import customtkinter as ctk
import pymysql
import hashlib

# Initialize app
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MOH Login")
        self.geometry("300x00")

        # Login Frame
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(self.frame, text="Login", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Username Entry
        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        # Password Entry
        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)

        # Login Button
        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Status Label
        self.status_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hash password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Database connection
        conn = pymysql.connect(host='localhost', user='root', password='', db='moh_db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE username=%s AND password=%s", (username, hashed_password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.status_label.configure(text="✅ Login Successful!", text_color="green")
            self.destroy()  # Close login window
            open_dashboard()  # Redirect to Dashboard
        else:
            self.status_label.configure(text="❌ Invalid Credentials", text_color="red")

# Function to open Dashboard
def open_dashboard():
    dashboard = ctk.CTk()
    dashboard.title("MOH Healthcare Management System")
    dashboard.geometry("800x500")

    label = ctk.CTkLabel(dashboard, text="Welcome to the Dashboard!", font=("Arial", 18))
    label.pack(pady=20)

    dashboard.mainloop()

# Run app
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
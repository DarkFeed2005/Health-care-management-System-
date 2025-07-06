import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import subprocess  # To open dashboards

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="**********", database="moh_healthcare")
cursor = conn.cursor()

def login():
    username = user_entry.get()
    password = pass_entry.get()
    role = role_var.get()

    cursor.execute(f"SELECT * FROM users WHERE email='{username}' AND password='{password}' AND role='{role}'")
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login", f"Welcome {username} as {role}")
        app.destroy()  # Close login window
        
        # Redirect to respective dashboard
        if role == "SuperAdmin":
            subprocess.run(["python", "super_admin_dash.py"])
        elif role == "Admin":
            subprocess.run(["python", "admin_dash.py"])
        elif role == "User":
            subprocess.run(["python", "user_dash.py"])
    else:
        messagebox.showerror("Error", "Invalid credentials!")

def open_reset_password():
    app.destroy()
    subprocess.run(["python", "reset_password.py"])  # Open password reset page

app = ctk.CTk()
app.geometry("400x300+325+175")
app.title("MOH Healthcare Login")
app.configure(fg_color="#1E2A38")

ctk.CTkLabel(app, text="Username:", text_color="#FFFFFF").pack()
user_entry = ctk.CTkEntry(app, width=200)
user_entry.pack()

ctk.CTkLabel(app, text="Password:", text_color="#FFFFFF").pack()
pass_entry = ctk.CTkEntry(app, show="*", width=200)
pass_entry.pack()

ctk.CTkLabel(app, text="Select Role:", text_color="#FFFFFF").pack()
role_var = ctk.StringVar(value="User")
role_menu = ctk.CTkComboBox(app, variable=role_var, values=["SuperAdmin", "Admin", "User"])
role_menu.pack()

ctk.CTkButton(app, text="Login", command=login, fg_color="#0084FF", hover_color="#4CC9F0").pack(pady=10)
ctk.CTkButton(app, text="Forgot Password?", command=open_reset_password, fg_color="#FF6B6B", hover_color="#FF9999").pack(pady=10)

app.mainloop()
 
 
 
 
 

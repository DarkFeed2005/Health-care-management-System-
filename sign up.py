import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import subprocess  # To open login.py

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="*********", database="moh_healthcare")
cursor = conn.cursor()

def register():
    name = name_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    role = role_var.get()

    # Check if email already exists
    cursor.execute(f"SELECT * FROM users WHERE email='{email}'")
    if cursor.fetchone():
        messagebox.showerror("Error", "Email already registered! Redirecting to login...")
        app.destroy()
        subprocess.run(["python", "login.py"])  # Open login page
        return

    # Insert new user into database
    cursor.execute(f"INSERT INTO users (name, email, password, role) VALUES ('{name}', '{email}', '{password}', '{role}')")
    conn.commit()
    messagebox.showinfo("Success", "Registration successful! Redirecting to login...")
    
    app.destroy()
    subprocess.run(["python", "login.py"])  # Open login page

app = ctk.CTk()
app.geometry("400x400")
app.title("MOH Healthcare Sign-Up")
app.configure(fg_color="#1E2A38")

ctk.CTkLabel(app, text="Full Name:", text_color="#FFFFFF").pack()
name_entry = ctk.CTkEntry(app, width=200)
name_entry.pack()

ctk.CTkLabel(app, text="Email:", text_color="#FFFFFF").pack()
email_entry = ctk.CTkEntry(app, width=200)
email_entry.pack()

ctk.CTkLabel(app, text="Password:", text_color="#FFFFFF").pack()
pass_entry = ctk.CTkEntry(app, show="*", width=200)
pass_entry.pack()

ctk.CTkLabel(app, text="Select Role:", text_color="#FFFFFF").pack()
role_var = ctk.StringVar(value="User")
role_menu = ctk.CTkComboBox(app, variable=role_var, values=["SuperAdmin", "Admin", "User"])
role_menu.pack()

ctk.CTkButton(app, text="Sign Up", command=register, fg_color="#0084FF", hover_color="#4CC9F0").pack(pady=10)
ctk.CTkButton(app, text="Already have an account? Login", command=lambda: subprocess.run(["python", "login.py"]), fg_color="#33CC99", hover_color="#4CC9F0").pack(pady=10)

app.mainloop()
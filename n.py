import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="$Kalana$12", database="moh_healthcare")
cursor = conn.cursor()

def login():
    username = user_entry.get()
    password = pass_entry.get()
    role = role_var.get()

    cursor.execute(f"SELECT * FROM users WHERE email='{username}' AND password='{password}' AND role='{role}'")
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login", f"Welcome {username} as {role}")
    else:
        messagebox.showerror("Error", "Invalid credentials!")

app = ctk.CTk()
app.geometry("400x300+750+300")
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





app.mainloop()
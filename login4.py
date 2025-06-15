import customtkinter as ctk
from tkinter import messagebox

def login():
    username = user_entry.get()
    password = pass_entry.get()
    role = role_var.get()

    # Logic to verify credentials from MySQL Database
    if username == "admin" and password == "admin123":
        messagebox.showinfo("Login", f"Welcome {username} as {role}")
    else:
        messagebox.showerror("Error", "Invalid credentials!")

app = ctk.CTk()
app.geometry("400x380+750+275")
app.title("MOH Healthcare Login")

ctk.CTkLabel(app, text="Username:").pack()
user_entry = ctk.CTkEntry(app)
user_entry.pack()

ctk.CTkLabel(app, text="Password:").pack()
pass_entry = ctk.CTkEntry(app, show="*")
pass_entry.pack()

ctk.CTkLabel(app, text="Select Role:").pack()
role_var = ctk.StringVar(value="User")
roles = ["SuperAdmin", "Admin", "User"]
role_menu = ctk.CTkComboBox(app, variable=role_var, values=roles)
role_menu.pack()

ctk.CTkButton(app, text="Login", command=login).pack()
app.mainloop()
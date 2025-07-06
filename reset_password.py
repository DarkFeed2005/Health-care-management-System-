import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import subprocess  # To open login.py


conn = mysql.connector.connect(host="localhost", user="root", password="*********", database="moh_healthcare")
cursor = conn.cursor()

def reset_password():
    username = user_entry.get()
    new_password = pass_entry.get()

    cursor.execute(f"SELECT * FROM users WHERE email='{username}'")
    if cursor.fetchone():
        cursor.execute(f"UPDATE users SET password='{new_password}' WHERE email='{username}'")
        conn.commit()
        messagebox.showinfo("Success", "Password updated! Redirecting to login...")
        app.destroy()
        #path
        subprocess.run(["python", "C:\\Users\\kalan\\OneDrive\\Desktop\\MOH Health Care System\\Health-care-management-System-\\login.py"])
    else:
        messagebox.showerror("Error", "Username not found! Contact Admin.")
        

app = ctk.CTk()
app.geometry("400x300+750+475")
app.title("Reset Password")
app.configure(fg_color="#1E2A38")

ctk.CTkLabel(app, text="Enter Registered Email:", text_color="#FFFFFF").pack()
user_entry = ctk.CTkEntry(app, width=200)
user_entry.pack()

ctk.CTkLabel(app, text="Enter New Password:", text_color="#FFFFFF").pack()
pass_entry = ctk.CTkEntry(app, show="*", width=200)
pass_entry.pack()

ctk.CTkButton(app, text="Reset Password", command=reset_password, fg_color="#FF6B6B", hover_color="#FF9999").pack(pady=10)

app.mainloop()
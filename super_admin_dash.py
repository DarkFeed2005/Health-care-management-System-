import customtkinter as ctk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry  
from PIL import Image
import subprocess

# Connect to DB
conn = mysql.connector.connect(host="localhost", user="root", password="$Kalana$12", database="moh_healthcare")
cursor = conn.cursor()

# Create Dashboard 
dashboard = ctk.CTk()
dashboard.geometry("900x600")
dashboard.title("SuperAdmin Dashboard")
dashboard.configure(fg_color="#1E2A38")

# Sidebar with Hover 
sidebar = ctk.CTkFrame(dashboard, width=150, fg_color="#273746")
sidebar.grid(row=0, column=0, rowspan=5, sticky="ns")

def expand_sidebar(event):
    for i in range(150, 250, 10):  # Smooth Expansion
        dashboard.after(10, lambda: sidebar.configure(width=i))

def collapse_sidebar(event):
    for i in range(250, 150, -10): 
        dashboard.after(10, lambda: sidebar.configure(width=i))

sidebar.bind("<Enter>", expand_sidebar)
sidebar.bind("<Leave>", collapse_sidebar)

# Load individual icons
profile_icon = ctk.CTkImage(Image.open("icons/profile.png"), size=(20, 20))
dashboard_icon = ctk.CTkImage(Image.open("icons/dashboard.png"), size=(20, 20))
notes_icon = ctk.CTkImage(Image.open("icons/notes.png"), size=(20, 20))
events_icon = ctk.CTkImage(Image.open("icons/events.png"), size=(20, 20))
add_icon = ctk.CTkImage(Image.open("icons/add.png"), size=(20, 20))
items_icon = ctk.CTkImage(Image.open("icons/items.png"), size=(20, 20))

# Sidebar Buttons with Icons
ctk.CTkButton(sidebar, text="Profile", image=profile_icon, fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Dashboard", image=dashboard_icon, fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Notes", image=notes_icon, fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Events", image=events_icon, fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Add New", image=add_icon, fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Items", image=items_icon, fg_color="#0084FF").pack(pady=10)

# Logout Confirmation Popup
def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to log out?"):
        dashboard.destroy()  # Close the dashboard
        subprocess.run(["python", "login.py"])  # Open the login page

# Log Out Button (Bottom) with Confirmation
ctk.CTkButton(sidebar, text="Log Out", command=logout, fg_color="#FF6B6B", hover_color="#FF9999").pack(side="bottom", pady=20)

# Main Container for Graphs & Filters
main_frame = ctk.CTkFrame(dashboard, fg_color="#1E2A38")
main_frame.grid(row=0, column=1, sticky="nsew")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

# Date Filter for Analytics
ctk.CTkLabel(main_frame, text="Select Date:", text_color="#FFFFFF").pack()
date_picker = DateEntry(main_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
date_picker.pack()

def filter_data():
    selected_date = date_picker.get_date()
    cursor.execute(f"SELECT COUNT(*) FROM medicines WHERE entry_date='{selected_date}'")
    medicines_count = cursor.fetchone()[0]

    cursor.execute(f"SELECT COUNT(*) FROM appointments WHERE appointment_date='{selected_date}'")
    appointments_count = cursor.fetchone()[0]

    messagebox.showinfo("Filtered Data", f"Medicines Added: {medicines_count}\nAppointments: {appointments_count}")

ctk.CTkButton(main_frame, text="Filter Analytics", command=filter_data, fg_color="#33CC99", hover_color="#4CC9F0").pack(pady=10)

# Live Updating Charts
def update_charts(frame):
    # Fetch User Counts
    cursor.execute("SELECT COUNT(*) FROM users WHERE role='SuperAdmin'")
    superadmins = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM users WHERE role='Admin'")
    admins = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM users WHERE role='User'")
    users = cursor.fetchone()[0]

    # Fetch Medicines and Patients
    cursor.execute("SELECT COUNT(*) FROM medicines")
    medicines = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM appointments")
    patients = cursor.fetchone()[0]

    # Clear previous graphs
    ax1.clear()
    ax2.clear()

    # Pie Chart (User Roles)
    labels = ["SuperAdmins", "Admins", "Users"]
    sizes = [superadmins, admins, users]
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["#33CC99", "#0084FF", "#FF6B6B"])
    ax1.set_title("User Distribution")

    # Bar Graph (Medicines & Patients)
    categories = ["Medicines", "Patients"]
    values = [medicines, patients]
    ax2.bar(categories, values, color=["#FF6B6B", "#0084FF"])
    ax2.set_title("Medicine & Patient Statistics")

ani = animation.FuncAnimation(fig, update_charts, frames=10, interval=2000)
plt.show()

dashboard.mainloop()
import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")
app.title("MOH Healthcare Dashboard")

# Sidebar Frame
sidebar = ctk.CTkFrame(app, width=150, fg_color="#273746")  # Default size
sidebar.grid(row=0, column=0, rowspan=4, sticky="ns")
ctk.CTkButton(sidebar, text="Dashboard", fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Manage Medicines", fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Appointments", fg_color="#0084FF").pack(pady=10)
ctk.CTkButton(sidebar, text="Reports & Analytics", fg_color="#0084FF").pack(pady=10)

def expand_sidebar(event):
    sidebar.configure(width=250)  # Expands smoothly

def collapse_sidebar(event):
    sidebar.configure(width=150)  # Returns to default size

sidebar.bind("<Enter>", expand_sidebar)
sidebar.bind("<Leave>", collapse_sidebar)

def highlight_hover(event):
    event.widget.configure(fg_color="#4CC9F0")  # Light up on hover

def reset_hover(event):
    event.widget.configure(fg_color="#0084FF")  # Default color

# Apply hover effects to buttons
for btn in sidebar.winfo_children():
    btn.bind("<Enter>", highlight_hover)
    btn.bind("<Leave>", reset_hover)
    

app.mainloop()
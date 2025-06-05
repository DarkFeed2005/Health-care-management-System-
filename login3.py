import customtkinter as ctk
from PIL import Image, ImageTk

# main application window
root = ctk.CTk()
root.geometry("1080x720+300+165")
root.title("greenFeather Sign In")

# background image
bg_image = Image.open("background.jpeg")  
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = ctk.CTkCanvas(root, width=400, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

#  background for UI elements
frame = ctk.CTkFrame(root, fg_color="transparent")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Logo label
logo_label = ctk.CTkLabel(frame, text="MOH Login form", font=("Arial", 24))
logo_label.pack(pady=10)

# Sign In heading
heading_label = ctk.CTkLabel(frame, text="Sign In", font=("Arial", 20))
heading_label.pack(pady=5)

# Email input field
email_label = ctk.CTkLabel(frame, text="Email Address/User Name")
email_label.pack(pady=5)
email_entry = ctk.CTkEntry(frame, width=250)
email_entry.pack(pady=5)

# Password input field
password_label = ctk.CTkLabel(frame, text="Password")
password_label.pack(pady=5)
password_entry = ctk.CTkEntry(frame, show="*", width=250)
password_entry.pack(pady=5)

# Forgot Password link
forgot_password_label = ctk.CTkLabel(frame, text="Forgot Password?")
forgot_password_label.pack(pady=5)

# Sign In button
sign_in_button = ctk.CTkButton(frame, text="Sign In", width=250)
sign_in_button.pack(pady=10)

# Create Account link
create_account_label = ctk.CTkLabel(frame, text="Don't have an account? Create your account" )
create_account_label.pack(pady=10)

# Run the application
root.mainloop()
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("1000x680+325+175")
app.title("MOH Login")
app.resizable(0,0)


side_img_data = Image.open("side-img.png")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")
google_icon_data = Image.open("google-icon.png")

app.mainloop()
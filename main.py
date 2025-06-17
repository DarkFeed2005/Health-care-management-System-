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



side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(700, 680))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")


app.mainloop()
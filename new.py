
import customtkinter as ctk 
import matplotlib.pyplot as plt



data = [30, 50, 20]  # Example values
labels = ["PHI", "Midwives", "Staff"]

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title("Staff Distribution")
plt.show()
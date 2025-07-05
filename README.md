# MOH Healthcare Management System. 🏥  

A **role-based healthcare management system** designed for the **Ministry of Health (MOH) in Sri Lanka**, built using **Python (CustomTkinter) and MySQL**.

<p align="center">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="70" height="70"/> </a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="70" height="70"/> </a>
</p>

## 🔹 Features  
✅ **Authentication System** – Three user roles:  
   - **Super Admins** (MOH Doctors & Regional director of health services)  
   - **Admins** (Senior Public Health Inspectors & Public Health Inspectors)  
   - **Users** (Public individuals seeking healthcare services)  

✅ **Role-Based Dashboards** – Dynamic UI tailored for each user type.  
✅ **Medicine Inventory Management** – Track healthcare supplies.  
✅ **Dengue Risk Areas Monitoring** – Identify and manage high-risk zones.  
✅ **Secure MySQL Database** – Stores user data, inventory, and reports.  

## 📌 Tech Stack  
🔹 **Python** – CustomTkinter for a sleek UI.  
🔹 **MySQL** – Database management for authentication and healthcare records.  
🔹 **CustomTkinter** – Modern GUI framework for a smooth user experience.  

## 🚀 Installation  
1️⃣ **Clone the repository:**  
   ```bash
   git clone https://github.com/DarkFeed2005/Health-care-management-System.git
   cd Health-care-management-System
```

2️⃣ Install dependencies
```bash
pip install costomtkinter

pip install mysql-connector-python customtkinter matplotlib pillow
```
3️⃣ Set up MySQL Database

- Import moh_healthcare.sql into MySQL.
- Update config.py with your database credentials.
  
4️⃣ Run the application
```bash
python main.py
```
📂 Project Structure
```bash
Health-care-management-System/
│── database/          # SQL schema & queries  
│── ui/                # GUI components using CustomTkinter  
│── logic/             # Authentication & business logic  
│── assets/            # Images & resources  
│── main.py            # Entry point of the application  
│── README.md          # Project documentation  
```

📢 Contributors

👤 Kalana Yasassri – Developer

💡 Health-care-management-System – Project vision

📩 Want to contribute? Fork the repo, create a new branch, and submit a pull request!





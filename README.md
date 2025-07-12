# 🩸 Blood Bank Management System
A web-based application built using **Flask** and **MySQL** that enables users to manage donor information efficiently. This system allows admins to add, update, view, and delete donor records through a simple and intuitive web interface.

## 🔧 Features
🛡️ **Role-Based Structure** *(single admin view for now)*

📋 **Donor Management**:
  - Add new donors with full details
  - View all donors in a list
  - Update donor information
  - Delete donor records

🔍 **Search Functionality** *(can be extended)*

📅 **Track Last Donation Date** for each donor

📈 **Clean UI** using HTML and inline CSS with Jinja2 templates

## 🛠️ Tech Stack
|Layer	|Technology|
|------|------|
|Backend	|Python, Flask|
|Database	|MySQL (via PyMySQL)|
|Frontend	|HTML, Jinja2 Templates|
|Hosting	|Flask Dev Server|

## 📁 Folder Structure (Expected)
```
project/
├── templates/
│   ├── home.html
│   ├── add_donor.html
│   ├── update_donor.html
│   ├── view_donors.html (create this file)
├── static/             # (Optional: for CSS/JS/Images)
├── app.py
└── requirements.txt    # Optional: Python packages
```
## ⚙️ Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/Pallavi01bs/BloodBankManagementSystem.git
cd BloodBankManagementSystem
```

2. Install Dependencies
```bash
pip install flask pymysql
```
3. Configure MySQL
Create a MySQL database named blood__bank and the required donors table:
```
sql
CREATE DATABASE blood__bank;

USE blood__bank;

CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    blood_group VARCHAR(10),
    contact_number VARCHAR(15),
    address TEXT,
    last_donation_date DATE
);
```
4. Run the App
```bash
python app.py
```
Then open your browser and go to  http://localhost:5000

## 🔐 User Roles
Currently, the system supports a single admin view without authentication. You can extend it with Flask-Login for:

Admin (Full access)

Lab/Clinic Staff (Limited access)

## 📸 Screenshots
Add UI screenshots like below:

```md
![Home Page](screenshots/home.png)
![Add Donor](screenshots/add_donor.png)
![Update Donor](screenshots/update_donor.png)
```
## 📄 License
This project is licensed under the [MIT License](LICENSE).

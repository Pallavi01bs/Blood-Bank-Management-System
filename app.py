from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Configure MySQL Connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="pallavi@01",
    database="blood__bank"
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        contact_number = request.form['contact_number']
        address = request.form['address']
        last_donation_date = request.form['last_donation_date']

        cursor = db.cursor()
        query = "INSERT INTO donors (name, age, blood_group, contact_number, address, last_donation_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, blood_group, contact_number, address, last_donation_date))
        db.commit()
        return redirect(url_for('view_donors'))
    return render_template('add_donor.html')

@app.route('/view')
def view_donors():
    cursor = db.cursor()
    query = "SELECT * FROM donors"
    cursor.execute(query)
    donors = cursor.fetchall()
    return render_template('view_donors.html', donors=donors)

@app.route('/update/<int:donor_id>', methods=['GET', 'POST'])
def update_donor(donor_id):
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        contact_number = request.form['contact_number']
        address = request.form['address']
        last_donation_date = request.form['last_donation_date']

        query = "UPDATE donors SET name=%s, age=%s, blood_group=%s, contact_number=%s, address=%s, last_donation_date=%s WHERE donor_id=%s"
        cursor.execute(query, (name, age, blood_group, contact_number, address, last_donation_date, donor_id))
        db.commit()
        return redirect(url_for('view_donors'))

    query = "SELECT * FROM donors WHERE donor_id=%s"
    cursor.execute(query, (donor_id,))
    donor = cursor.fetchone()
    return render_template('update_donor.html', donor=donor)

@app.route('/delete/<int:donor_id>')
def delete_donor(donor_id):
    cursor = db.cursor()
    query = "DELETE FROM donors WHERE donor_id=%s"
    cursor.execute(query, (donor_id,))
    db.commit()
    return redirect(url_for('view_donors'))

if __name__ == '__main__':
    app.run(debug=True)
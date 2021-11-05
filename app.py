from flask import Flask, render_template, request,session,redirect,url_for
from flask_mysqldb import MySQL
import re
import mysql.connector
import MySQLdb.cursors 
from werkzeug.utils import redirect

app = Flask(__name__, template_folder = 'template', static_folder  = 'static')
app.secret_key="blood_donation"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'blood_donation_dbms'

mysql = MySQL(app) 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    msg=''
    if 'Email_id' in session:
        msg=session['Email_id']
        return render_template('home.html',msg=msg)
    return redirect(url_for('index'))

@app.route("/user_login" ,methods=['POST','GET'])
def user_login():
    msg = ""
    if request.method=='POST'and "Email_id" in request.form and "Password" in request.form :
        Email_id=request.form['Email_id']
        Password=request.form['Password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Donor WHERE Email_id=%s ',(Email_id,))
        account=cursor.fetchone()
        cursor.close()
        if account and account['Password']==Password:
            session['loggedin']=True
            session['Email_id'] = Email_id
            session['Phone_num'] = account['Phone_num']
            session['First_name'] = account['First_name']
            session['Last_name'] = account['Last_name']
            return render_template('home.html')
        else:
            msg='Incorrect username/password!'  
    else:
        msg = " Please fill the form !"  
    return render_template('user_login.html',msg=msg)

@app.route("/user_logout")
def user_logout():
    session.pop('loggedin',None)
    session.pop('Email_id',None)
    session.pop('Phone_num',None)
    session.pop('First_name',None)
    session.pop('Last_name',None)
    return redirect(url_for('user_login'))


@app.route("/user_signup",methods=['POST','GET'])
def user_signup():
    msg=''
    if request.method=='POST' and  'First_name' in request.form and 'Gender' in request.form and 'Email_id' in request.form and 'Last_name' in request.form and 'Age' in request.form and 'Phone_num' in request.form and  'Password' in request.form and 'c_password' in request.form and 'Street' in request.form and 'Blood_group' in request.form and 'eligibility' in request.form and 'Frequent' in request.form and 'City' in request.form and 'District' in request.form and 'State' in request.form and 'Pincode' in request.form :
        First_name=request.form['First_name']
        Last_name=request.form['Last_name']
        Email_id=request.form['Email_id']
        Gender=request.form['Gender']
        Age=request.form['Age']
        Phone_num=request.form['Phone_num']
        Password=request.form['Password']
        c_password=request.form['c_password']
        Street=request.form['Street']
        Blood_group=request.form['Blood_group']
        Eligibility=request.form['eligibility']
        Frequent=request.form['Frequent']
        City=request.form['City']
        District=request.form['District']
        State=request.form['State']
        Pincode=request.form['Pincode']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Donor WHERE Email_id= % s', (Email_id, ))
        account1=cursor.fetchone()
        cursor.execute('SELECT * FROM Donor WHERE Phone_num= % s', (Phone_num, ))
        account2=cursor.fetchone()
        cursor.close()
        if account1 :
            msg="An account is already registered with this email."
        elif account2 :
            msg="An account is already registered with this Phone Number."
        elif not re.match(r'[0-9]+', Phone_num):
            msg = 'Invalid Phone number !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email_id):
            msg = 'Invalid email address !'
        elif len(Phone_num) != 10:
            msg = 'Please enter a 10 digit correct phone number !'
        elif len(Password) < 8:
            msg = 'Password must containe atleast 8 digits or characters !'
        elif (Password != c_password):
            msg="Password does not match! "
        elif not Phone_num or not Password or not Email_id:
            msg = 'Please fill out the form !'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO Donor(First_name,Last_name,Email_id,Age,Phone_num,Password,Street,Blood_group,Eligibility,Frequent_Donor,City,District,State,Pincode,Gender) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (First_name,Last_name,Email_id,Age,Phone_num,Password,Street,Blood_group,Eligibility,Frequent,City,District,State,Pincode,Gender))
            mysql.connection.commit()
            session['loggedin'] = True
            session['Email_id'] = Email_id
            session['Phone_num'] = Phone_num
            session['First_name'] = First_name
            session['Last_name'] = Last_name
            cursor.close()
            return redirect(url_for('home'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    
    return render_template('user_signup.html', msg = msg)

@app.route("/bloodbank_registeration",methods=['POST','GET'])
def bloodbank_registeration():
    msg=""
    if request.method=='POST' and "Blood_bank_name" in request.form and "License_number" in request.form and "Owner_name" in request.form and "Phone_number" in request.form and "Email" in request.form and "Password" in request.form and "c_password" in request.form and "Street" in request.form and "City" in request.form and "Pincode" in request.form and "District" in request.form and "State" in request.form  and "Website" in request.form :
        Blood_bank_name=request.form['Blood_bank_name']
        License_number=request.form['License_number']
        Owner_name=request.form['Owner_name']
        Phone_number=request.form['Phone_number']
        Email=request.form['Email']
        Password=request.form['Password']
        c_password=request.form['c_password']
        Street=request.form['Street']
        Website=request.form['Website']
        City=request.form['City']
        District=request.form['District']
        State=request.form['State']
        Pincode=request.form['Pincode']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Blood_bank WHERE License_number= % s', (License_number, ))
        account1=cursor.fetchone()
        cursor.execute('SELECT * FROM Blood_bank WHERE Phone_number= % s', (Phone_number, ))
        account2=cursor.fetchone()
        cursor.execute('SELECT * FROM Blood_bank WHERE Email= % s', (Email, ))
        account3=cursor.fetchone()
        cursor.close()
        if account1 :
            msg="A Blood bank with this license number already exists."
        elif account2 :
            msg="This phone number is already registered with a blood bank."
        elif account3 :
            msg="This email is already registered with a blood bank."
        elif not re.match(r'[0-9]+', Phone_number):
            msg = 'Invalid Phone number !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
            msg = 'Invalid email address !'
        elif len(Phone_number) != 10:
            msg = 'Please enter a 10 digit correct phone number !'
        elif len(Password) < 8:
            msg = 'Password must containe atleast 8 digits or characters !'
        elif (Password != c_password):
            msg="Password does not match! "
        elif not Phone_number or not Password or not Email or not License_number or not Blood_bank_name or not Owner_name:
            msg = 'Please fill out the form !'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO Blood_bank(Password,License_number,Blood_bank_name,Owner_name,Email,Phone_number,Street,Pincode,City,District,State,Website) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Password,License_number,Blood_bank_name,Owner_name,Email,Phone_number,Street,Pincode,City,District,State,Website))
            mysql.connection.commit()
            msg='Form Submitted. You can login once your application is approved.'
            session['loggedin'] = True
            session['Email'] = Email
            session['Phone_number'] = Phone_number
            session['License_number'] = License_number
            session['Blood_bank_name'] = Blood_bank_name
            cursor.close()
    elif request.method == 'POST':
        msg = 'Please fill  the form !'
    return render_template('blood_bank_regis_me.html',msg=msg)

@app.route("/blood_bank_login",methods=['POST','GET'])
def blood_bank_login():
    msg=''
    if request.method=='POST'and "License_number" in request.form and "Password" in request.form :
        License_number=request.form['License_number']
        Password=request.form['Password']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Blood_bank WHERE License_number=%s ',(License_number,))
        account=cursor.fetchone()
        cursor.close()
        if account and account['Password']==Password:
            session['loggedin'] = True
            session['Email'] = account['Email']
            session['Phone_number'] = account['Phone_number']
            session['License_number'] = account['License_number']
            session['Blood_bank_name'] = account['Blood_bank_name']
            return render_template('')
        else:
            msg="Incorrect username/password!"
    else:
        msg = " Please fill the form !" 
    return render_template('blood_bank_login.html',msg=msg)        

@app.route("/bank_logout")
def bank_logout():
    session.pop('loggedin',None)
    session.pop('License_number',None)
    return redirect(url_for('blood_bank_login'))


@app.route("/check_blood_availability")
def check_blood_availability():
    return render_template('check_blood_availability.html')

@app.route("/admin_login",methods=['GET','POST'])
def admin_login():
    msg=''
    if request.method=='POST'and "Email_id" in request.form and "Password" in request.form :
        Email=request.form['Email_id']
        Password=request.form['Password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Admin WHERE Email=%s ',(Email,))
        account=cursor.fetchone()
        cursor.close()
        if account and account['Password']==Password:
            session['loggedin']=True
            session['Email'] = Email
           
            return render_template('admin_dashboard.html')
        else:
            msg='Incorrect username/password!'  
    else:
        msg = " Please fill the form !" 
    return render_template('admin_login.html',msg=msg)

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)
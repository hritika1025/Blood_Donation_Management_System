from flask import Flask, render_template, request,session,redirect, sessions,url_for
from flask_mysqldb import MySQL
import re
import mysql.connector
import MySQLdb.cursors 
from werkzeug.utils import redirect
from datetime import date, datetime, timedelta
import datetime

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
        Frequent_donor = request.form['Frequent']
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
            cursor.execute('INSERT INTO Donor(First_name,Last_name,Email_id,Age,Phone_num,Password,Street,Blood_group,Eligibility,Frequent_Donor,City,District,State,Pincode,Gender) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (First_name,Last_name,Email_id,Age,Phone_num,Password,Street,Blood_group,Eligibility,Frequent_donor,City,District,State,Pincode,Gender))
            mysql.connection.commit()
            session['loggedin'] = True
            session['Email_id'] = Email_id
            session['Phone_num'] = Phone_num
            session['First_name'] = First_name
            session['Last_name'] = Last_name
            session['Age'] = Age
            session['Blood_group'] = Blood_group
            session['Eligibility'] = Eligibility
            session['Frequent_donor'] = Frequent_donor
            session['Street'] = Street
            session['District'] = District
            session['City'] = City
            session['State'] = State
            cursor.close()
            return redirect(url_for('home'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    
    return render_template('user_signup.html', msg = msg)

@app.route("/user_profile")
def user_profile():
    if session['loggedin'] == True :
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Donor WHERE Email_id = %s', (session['Email_id']))
        user_details = cursor.fetchall()

    return render_template('user_profile.html', First_name = session['First_name'], 
                            Last_name = session['Last_name'], Phone_num = session['Phone_num'], 
                            Age = session['Age'], Eligibility = session['Eligibility'], Frequent_donor =
                            session['Frequent_donor'], City = session['City'], District = 
                            session['District'], Street = session['Street'], State = session['State']
                             )

@app.route("/edit_user_profile", methods=['POST','GET'])
def edit_user_profile() :
    if request.method == 'POST' :
        First_name=request.form['First_name']
        Last_name=request.form['Last_name']
        Gender=request.form['Gender']
        Age=request.form['Age']
        Phone_num=request.form['Phone_num']
        Password=request.form['Password']
        Street=request.form['Street']
        Blood_group=request.form['Blood_group']
        Eligibility=request.form['eligibility']
        Frequent_donor = request.form['Frequent']
        City=request.form['City']
        District=request.form['District']
        State=request.form['State']
        Pincode=request.form['Pincode']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE DONOR SET First_name = %s AND Last_name = %s AND Gender = %s AND Age = %s AND Phone_num = %s AND Password = %s AND Street = %s AND Blood_group = %s AND Eligibility = %s AND Frequent_donor = %s AND City = %s AND District = %s AND State = %s AND Pincode = %s', (First_name, Last_name, Gender, Age, Phone_num, Password, Street, Blood_group, Eligibility, Frequent_donor, City, District, State, Pincode,))
        mysql.connection.commit()
        return render_template('edit_user_profile.html')
    
    else :
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Donor WHERE Email_id = %s', (session['Email_id']))
        user_details = cursor.fetchall()

    return render_template('edit_user_profile.html', First_name = session['First_name'], 
                            Last_name = session['Last_name'], Phone_num = session['Phone_num'], 
                            Age = session['Age'], Eligibility = session['Eligibility'], Frequent_donor =
                            session['Frequent_donor'], City = session['City'], District = 
                            session['District'], Street = session['Street'], State = session['State']
                             )

@app.route('/user_non_edit_profile')
def user_non_edit_profile() :
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Donor WHERE Email_id = %s', (session['Email_id']))
    user_details = cursor.fetchall()
    return render_template('user_non_edit_profile.html', First_name = session['First_name'], 
                            Last_name = session['Last_name'], Phone_num = session['Phone_num'], 
                            Age = session['Age'], Eligibility = session['Eligibility'], Frequent_donor =
                            session['Frequent_donor'], City = session['City'], District = 
                            session['District'], Street = session['Street'], State = session['State']
                             )


@app.route('/search_blood_banks', methods = ['GET', 'POST'])
def search_blood_banks():
    msg = ''
    if request.method == "POST":
        State = request.form['State']
        District = request.form['District']
        Blood_group = request.form['Blood_group']
        if len(State) > 0 and len(District) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute('INSERT INTO record VALUES (NULL, % s, % s, % s,% s)',(username , state, district, bloodgroup,))
            # mysql.connection.commit()
            # if bloodgroup in ('SELECT Blood_Group From Blood_stock WHERE License_Number in (SELECT License_Number FROM Blood_bank WHERE State = %s AND District = %s', (State, District)):
            print(Blood_group)
            # session['bloodgroup'] = Blood_group
            cursor.execute('SELECT Blood_bank_name, Phone_number, Website, Street, Pincode  FROM Blood_bank WHERE State = %s AND District = %s', (State, District,))
            rows = cursor.fetchall()
            # for row in rows:
            #     row = row
            cursor.close()
            return render_template('search_blood_banks.html', rows = rows)
            # return render_template('check_blood_availability.html', msg = "Sorry! No data available.")
        else:
            msg = "Please fill all the details!"
            return render_template('search_blood_banks.html', msg = msg)
    return render_template('search_blood_banks.html')


@app.route("/bloodbank_registration",methods=['POST','GET'])
def bloodbank_registration():
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
        cursor.execute('SELECT * FROM Blood_bank WHERE License_number=%s AND Verification="Accept"',(License_number,))
        account=cursor.fetchone()
        cursor.close()
        if account and account['Password']==Password:
            session['loggedin'] = True
            session['Email'] = account['Email']
            session['Phone_number'] = account['Phone_number']
            session['License_Number'] = account['License_Number']
            session['Blood_bank_name'] = account['Blood_bank_name']
            return render_template('home.html')
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


@app.route("/check_blood_availability", methods = ['GET', 'POST'])
def check_blood_availability():
    msg = ''
    if request.method == "POST":
        State = request.form['State']
        District = request.form['District']
        Blood_group = request.form['Blood_group']
        if len(State) > 0 and len(District) > 0 and len(Blood_group) >0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute('INSERT INTO record VALUES (NULL, % s, % s, % s,% s)',(username , state, district, bloodgroup,))
            # mysql.connection.commit()
            # if bloodgroup in ('SELECT Blood_Group From Blood_stock WHERE License_Number in (SELECT License_Number FROM Blood_bank WHERE State = %s AND District = %s', (State, District)):
            print(Blood_group)
            # session['bloodgroup'] = Blood_group
            cursor.execute('SELECT Blood_bank_name, Street FROM Blood_bank WHERE State = %s AND District = %s AND License_Number in (SELECT License_Number FROM Blood_stock WHERE Blood_group = %s)', (State, District, Blood_group,))
            rows = cursor.fetchall()
            # for row in rows:
            #     row = row
            cursor.close()
            return render_template('blood_avail.html', rows = rows)
            # return render_template('check_blood_availability.html', msg = "Sorry! No data available.")
        else:
            msg = "Please fill all the details!"
            return render_template('check_blood_availability.html', msg = msg)
    return render_template('check_blood_availability.html')

@app.route("/edit_blood_stock")    
def edit_blood_stock():
    msg=''
    if session['loggedin'] == True :
        if request.method=='POST'and "Blood_group" in request.form and "Adding_date" in request.form and "Removing_date" in request.form and "Units_added" in request.form and "Units_removed" in request.form :
            Blood_group=request.form['Blood_group']
            Date=request.form['Date']
            Units_added=request.form['Units_added']
            Units_removed=request.form['Units_removed']
            License_number=session['License_number']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO Blood_stock(License_number, Blood_group,Date,Units_added, Units_removed)',(License_number,Blood_group,Units_added,Units_removed,))
            msg="Record Added"
            mysql.connection.commit()
            cursor.close()
        else:
            msg = " Please fill the form !" 
    else:
        return redirect(url_for('blood_bank_login'))
    return render_template('edit_blood_stock.html',msg=msg)   

@app.route("/blood_bank_profile")
def blood_bank_profile():
    msg=''
    if session['loggedin'] == True :
        if request.method=='POST':
            Blood_bank_name=request.form['Blood_bank_name']
            Owner_name=request.form['Owner_name']
            Phone_number=request.form['Phone_number']
            Password=request.form['Password']
            Website=request.form['Website']
            Weekday=request.form['Weekday']
            Opening_time=request.form['Opening_time']
            Closing_time=request.form['Closing_time']
            Street=request.form['Street']
            City=request.form['City']
            Pincode=request.form['Pincode']
            District=request.form['District']
            State=request.form['State']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO Blood_bank(Blood_bank_name,Owner_name,Phone_number,Password,Website,Weekday,Opening_time,Closing_time,Street,City,Pincode,District,State)',(Blood_bank_name,Owner_name,Phone_number,Password,Website,Weekday,Opening_time,Closing_time,Street,City,Pincode,District,State,))
            msg="Data Edited"
            mysql.connection.commit()
            cursor.close()
        else:
            msg = " Please Edit the form !" 
        return render_template('blood_bank_profile.html',msg=msg, Blood_bank_name = session['Blood_bank_name'], Owner_name = session['Owner_name'], Phone_number = session['Phone_number'], Password = session['Password'], Website = session['Website'], Weekday =session['Weekday'],Opening_time =session['Opening_time'],Closing_time =session['Closing_time'], Street = session['Street'],  City = session['City'],Pincode=session['Pincode'], District = session['District'], State = session['State'])
    else:
        return redirect(url_for('blood_bank_login'))
        

        # ADMIN PART :

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template('admin_dashboard.html')

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

@app.route('/registeration_verification_by_admin',methods=['GET','POST']) 
def registeration_verification_by_admin() :
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Blood_bank WHERE Verification="Not Verified"')
    rows = cursor.fetchall()
    cursor.close()
    if request.method=='POST'and "License_number" in request.form and "result" in request.form :
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        License_number=request.form['License_number']
        result=request.form['result']
        cursor.execute('UPDATE Blood_bank SET Verification = %s WHERE License_number=%s',(result,License_number,))
        mysql.connection.commit()
        cursor.close()
    return render_template('registeration_verification_by_admin.html',rows=rows)


# @app.route('/contact', methods = ['GET', 'POST'])
# def contact():
#     msg = ''
#     if request.method == 'POST' :
#         Name = request.form['Name']
#         Email_id = request.form['Email_id']
#         phone_num = request.form['phone_num']
#         Message = request.form['Message']
#         Date = request.form['Date']
#         if len(Name) > 0 and len(Email_id) > 0 and len(phone_num) > 0 and len(Message) > 0 and len(Date) >0:
#             cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             cursor.execute('INSERT INTO Message_to_admin VALUES (NULL, % s, % s, % s,% s, %s)',(Name, Email_id, phone_num, Message, Date,))
#             mysql.connection.commit()
#             session['Name'] = Name
#             session['Email_id'] = Email_id
#             session['phone_num'] = phone_num
#             session['Message'] = Message
#             session['Date'] = Date
#             cursor.close()
#             return render_template('contact.html', msg = "Your message has been successfully sent to the admin.")
#         else :
#             return render_template('contact.html', msg = "Please fill out the form")
#     return render_template('contact.html')

@app.route("/contact",methods=['GET','POST'])
def contact():
    msg=''
    if request.method=='POST'and "Email_id" in request.form and "phone_num" in request.form and "Name" in request.form and "Date" in request.form:
        Name=request.form['Name']
        Email_id=request.form['Email_id']
        phone_num=request.form['phone_num']
        Message=request.form['Message']
        Date=request.form['Date']
        if not re.match(r'[0-9]+', phone_num):
            msg = 'Invalid Phone number !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email_id):
            msg = 'Invalid email address !'
        elif len(phone_num) != 10:
            msg = 'Please enter a 10 digit correct phone number !'
        elif len(Message) > 5000:
            msg = 'Message is too long!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO Message_to_admin (Id, Name, Email_id,phone_num,Message,Date) VALUES(NULL, %s,%s,%s,%s,%s)', (Name,Email_id,phone_num,Message,Date,))
            mysql.connection.commit()
            session['Name'] = Name
            session['Email_id'] = Email_id
            session['phone_num'] = phone_num
            session['Message'] = Message
            session['Date'] = Date
            msg='Message Sent'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('contact.html',msg=msg)

@app.route('/user_msg_to_admin')
def user_msg_to_admin() :
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    current_date = date.today()
    days = datetime.timedelta(7)
    new_date = current_date - days
    # cursor.execute('SELECT * FROM record WHERE username = % s AND date >= %s ORDER BY date DESC', (session['username'], new_date))
    cursor.execute('SELECT * FROM Message_to_admin WHERE Date >= %s ORDER BY Date DESC', (new_date,))
    rows = cursor.fetchall()
    
    return render_template("user_msg_to_admin.html", rows = rows)

        

app.run(debug=True)
from flask import Flask, render_template, request,session,redirect,url_for
from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb.cursors 
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key="blood_donation"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'M25SQLpradeep'
app.config['MYSQL_DB'] = 'blood_management'

mysql = MySQL(app) 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user_login")
def user_login():
    if request.method=='POST'and "email" in request.form and "password" in request.form :
        email=request.form['email']
        password=request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM Donor WHERE Email_id=%s AND Password=%s",(email,password))
        account=cursor.fetchone()
        if account:
            session['loggedin']=True
            session['email']=email
            return render_template('')
        else:
            msg='Incorrect username/password!'    
    return render_template('user_login.html',msg=msg)

@app.route("/user_logout")
def user_logout():
    session.pop('loggedin',None)
    session.pop('email',None)
    return redirect(url_for(''))


    #     Query='''SELECT * FROM Donor WHERE Email_id =%s and password=%s''' ,(email,password)
    #     cur = myconn.cursor()
    #     cur.execute(Query)
    #     Details = cur.fetchone()
    #     if Details:
    #         return 
    #     else :
    #         msg='Incorrect username/password!'    
    # else:    
    #     return render_template('user_login.html')

@app.route("/user_signup",methods=['POST','GET'])
def user_signup():
    msg="Please fill all the elements of the form!"
    if request.method=='POST' and  "f_name" in request.form and "gender" in request.form and "email" in request.form and "l_name" in request.form and "age" in request.form and "phone_number" in request.form and  "password" in request.form and "c_password" in request.form and "address" in request.form and "blood_group" in request.form and "eligibility" in request.form and "fd" in request.form and "city" in request.form and "district" in request.form and "state" in request.form and "pincode" in request.form :
        f_name=request.form('f_name')
        l_name=request.form('l_name')
        email=request.form('email')
        gender=request.form('gender')
        age=request.form('age')
        phone_number=request.form('phone_number')
        password=request.form('password')
        c_password=request.form('c_password')
        address=request.form('address')
        blood_group=request.form('blood_group')
        eligibility=request.form('eligibility')
        fd=request.form('fd')
        city=request.form('city')
        district=request.form('district')
        state=request.form('state')
        pincode=request.form('pincode')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Donor WHERE Email_id=email')
        account=cursor.fetchone()
        if account :
            msg="An account had been registered with this email"
            return render_template('user_singup.html',msg=msg)
        
        elif (password != c_password):
            msg="Password and Confirm Password are not matching! "
            return render_template('user_signup_2.html',msg=msg,f_name=f_name,l_name=l_name,email=email,gender=gender,age=age,phone_number=phone_number,password=password,address=address,blood_group=blood_group,eligibility=eligibility,fd=fd,city=city,district=district,state=state,pincode=pincode)
        
        else:

            cursor.execute('INSERT INTO Donor(First_name,Last_name,Email_id,Age,Phone_num,Password,Address,Blood_group,Eligibility,Frequent,City,District,State,Pincode,Gender) VALUES(%s,%s,%s,%d,%d,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s)'(f_name,l_name,email,age,phone_number,password,address,blood_group,eligibility,fd,city,district,state,pincode,gender))
            mysql.connection.commit()
            return redirect(url_for('user_login'))
    return render_template('user_signup.html')
    # return render_template("user_signup2.html",f_name=f_name,l_name=l_name,username=username,age=age,phone_number=phone_number,password=password,)

@app.route("/blood_bank_registeration",methods=['POST','GET'])
def blood_bank_registeration():
    msg="Please fill all the elements of the form!"
    if request.method=='POST' and "name" in request.form and "lnum" in request.form and "oname" in request.form and "phn" in request.form and "email" in request.form and "password" in request.form and "c_password" in request.form and "address" in request.form and "city" in request.form and "pincode" in request.form and "district" in request.form and "state" in request.form and "weekday" in request.form and "otime" in request.form and "ctime" in request.form and "website" in request.form :
        details=request.form
        if (details['password']!=details['c_password']):
            msg="Password and Confirm Password are not matching! "
            return render_template('blood_bank_regis_2.html',msg=msg,name= details['name'],lnum=details['lnum'],oname=details['oname'],Phn=details['phn'],email=details['email'],password=details['password'],address=details['address'],city=details['city'],pincode=details['pincode'],district=details['district'],state=details['state'],website=details['website'],weekday=details['weekday'],otime=details['otime'],ctime=details['ctime'])
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.exceute("INSERT INTO Blood_bank(Blood_bank_name,License_number,Owner_name,Phone_number,Email,Password,Address,City,Pincode,District,State,Website) VALUES(%s,%s,%s,%d,%s,%s,%s,%s,%s,%s,%s,%s)"(details['name'],details['lnum'],details['oname'],details['phn'],details['email'],details['password'],details['address'],details['city'],details['pincode'],details['district'],details['state'],details['website']))
            cursor.execute("INSERT INTO Blood_bank_timings(License_number,Weekday,Opening_time,Closing_time) VALUES(%s,%s,%s,%s) "(details['lnum'],details['weekday'],details['otime'],details['ctime']))
            mysql.connection.commit()

    return render_template('blood_bank_regis_me.html')

@app.route("/blood_bank_login")
def blood_bank_login():
    msg=''
    if request.method=='POST'and "License number" in request.form and "password" in request.form :
        License=request.form['License number']
        password=request.form['password']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Blood_bank WHERE License_Number=%s AND password=%s'(License,password,))
        account=cursor.fetchone()
        if account:
            session['loggedin']=True
            session['License']=License
            return render_template('')
        else:
            msg="Incorrect username/password!"
    return render_template('blood_bank_login.html',msg=msg)        

@app.route("/bank_logout")
def bank_logout():
    session.pop('loggedin',None)
    session.pop('License',None)
    return redirect(url_for(''))


    #     Query='''SELECT * FROM Donor WHERE Email_id =%s and password=%s''' ,(email,password)
    #     cur = myconn.cursor()
    #     cur.execute(Query)
    #     Details = cur.fetchone()
    #     if Details:
    #         return 
    #     else :
    #         msg='Incorrect username/password!'    
    # else:    
    #     return render_template('user_login.html')
    # return render_template('blood_bank_login.html')

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)
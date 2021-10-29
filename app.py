from flask import Flask ,render_template

app = Flask(__name__, template = 'template', static = 'static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user_login")
def user_login():
    return render_template('user_login.html')

@app.route("/user_signup")
def user_signup():
    return render_template('user_signup.html')

@app.route("/blood_bank_registeration")
def blood_bank_registeration():
    return render_template('blood_bank_regis_me.html')

@app.route("/blood_bank_login")
def blood_bank_login():
    return render_template('blood_bank_login.html')

@app.route("/check_blood_availability")
def check_blood_availability():
    return render_template('check_blood_availability.html')

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mayurj@23'
app.config['MYSQL_DB'] = 'test2'
mysql = MySQL(app)

# Set a secret key for session management
app.secret_key = 'Mayurj@23'

@app.route('/')
def home():
    return render_template('userAccount.html')
    
@app.route('/contactUs', methods=['GET', 'POST'])
@app.route('/contactUs.html', methods=['GET', 'POST'])
def contactUs():
    if request.method == 'POST':
   	
        
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        cur = mysql.connection.cursor()
        sql = "INSERT INTO test2.contact ( name, email, message) VALUES ( %s, %s, %s)"
        val = ( name, email, message)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    
    return render_template('contactUs.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # Check if the credentials are valid
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password, name, age, gender, grade "
                    "FROM users "
                    "WHERE username = %s AND password = %s", (username, hashed_password))
        user = cur.fetchone()
        cur.close()
        
        if user:
            session['username'] = username
            return redirect('/')
        else:
            return 'Invalid credentials. Please try again.'
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()


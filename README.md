# Xenon_stack- Technical Round-2

Theme Of My Project Is College App

                                                              So I diveded Into In Three Parts


1. Front End - I Started with front end i use html to develope an frontend  
 frontend divided in three Part
 
 
 a.userAccount.html
 b.Login.html
 c.ContactUs.html
 
 
 a.userAccount.html
 here is my frond end code to take an input of username and password
 <!DOCTYPE html>
<html>
<head>
	<title>Logged In</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 0;
			padding: 0;
		}
		.container {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			min-height: 100vh;
			background-color: #f2f2f2;
		}
		.message {
			display: flex;
			align-items: center;
			justify-content: center;
			flex-direction: column;
			background-color: #fff;
			border-radius: 10px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
			max-width: 600px;
			width: 100%;
			padding: 20px;
			margin: 20px;
			text-align: center;
		}
		h1 {
			font-size: 2.5rem;
			margin: 0;
		}
		p {
			font-size: 1.5rem;
			margin: 20px 0;
		}
		a {
			display: inline-block;
			background-color: #007bff;
			color: #fff;
			padding: 10px 20px;
			border: none;
			border-radius: 5px;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
			text-decoration: none;
			cursor: pointer;
		}
		a:hover {
			background-color: #0069d9;
		}
		@media only screen and (max-width: 600px) {
			.message {
				max-width: 400px;
			}
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="message">
			<h1>You are logged in!</h1>
			<p>Thank you for logging in. You now have access to your account.</p>
			<a href="login.html">Log out</a>
		</div>
	</div>
</body>
</html>

			


![1](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/9ed31639-27e9-48d1-92e4-59a372414888)



b) Login.html

<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 0;
			padding: 0;
		}
		.container {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			min-height: 100vh;
			background-color: #f2f2f2;
		}
		form {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			padding: 20px;
			background-color: #fff;
			border-radius: 10px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
			max-width: 400px;
			width: 100%;
			margin: 20px;
		}
		input[type="text"], input[type="password"] {
			display: block;
			width: 100%;
			padding: 10px;
			margin: 10px 0;
			border: none;
			border-radius: 5px;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
		}
		input[type="submit"] {
			display: inline-block;
			background-color: #007bff;
			color: #fff;
			padding: 10px 20px;
			border: none;
			border-radius: 5px;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
			cursor: pointer;
		}
		input[type="submit"]:hover {
			background-color: #0069d9;
		}
		@media only screen and (max-width: 600px) {
			form {
				max-width: 300px;
			}
		}
		.ribbon {
			display: flex;
			justify-content: space-between;
			align-items: center;
			padding: 10px;
			background-color: #9ee42c;
			color: #fff;
			position: fixed;
			top: 0;
			left: 0;
			right: 0;
			z-index: 1;
		}
		.home-button, .contact-button {
			display: inline-block;
			background-color: #fff;
			color: #007bff;
			padding: 5px 10px;
			border-radius: 5px;
			text-decoration: none;
			font-weight: bold;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
			margin-right: 10px;
			cursor: pointer;
		}
		.home-button:hover, .contact-button:hover {
			background-color: #007bff;
			color: #fff;
		}
		@media only screen and (max-width: 600px) {
			.ribbon {
				flex-direction: column;
				align-items: center;
			}
			.home-button, .contact-button {
				margin: 10px 0;
			}
		}
	</style>
</head>
<body>
	<div class="ribbon">
		<a href="#" class="home-button">Home</a>
		<a href="contactUs.html" class="contact-button">Contact Us</a>
</div>
<div class="container">
		<form method="POST" action="/login">
        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">
    </form>
	</div>
</body>
</html>

c. Contact_us.html

<!DOCTYPE html>
<html>
<head>
	<title>Student Details Form</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		body {
			font-family: Arial, sans-serif;
			margin: 0;
			padding: 0;
		}
		.container {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			min-height: 100vh;
			background-color: #f2f2f2;
		}
		form {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			padding: 20px;
			background-color: #fff;
			border-radius: 10px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
			max-width: 600px;
			width: 100%;
			margin: 20px;
		}
		input[type="text"], input[type="email"], input[type="date"], select {
			display: block;
			width: 100%;
			padding: 10px;
			margin: 10px 0;
			border: none;
			border-radius: 5px;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
		}
		input[type="submit"] {
			display: inline-block;
			background-color: #007bff;
			color: #fff;
			padding: 10px 20px;
			border: none;
			border-radius: 5px;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
			cursor: pointer;
		}
		input[type="submit"]:hover {
			background-color: #0069d9;
		}
		label {
			font-weight: bold;
			margin-top: 20px;
		}
		@media only screen and (max-width: 600px) {
			form {
				max-width: 400px;
			}
		}
.ribbon {
			display: flex;
			justify-content: space-between;
			align-items: center;
			padding: 10px;
			background-color: #00ffff;
			color: #fff;
			position: fixed;
			top: 0;
			left: 0;
			right: 0;
			z-index: 1;
		}
		.home-button, .contact-button {
			display: inline-block;
			background-color: #fff;
			color: #007bff;
			padding: 5px 10px;
			border-radius: 5px;
			text-decoration: none;
			font-weight: bold;
			box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
			margin-right: 10px;
			cursor: pointer;
		}
		.home-button:hover, .contact-button:hover {
			background-color: #007bff;
			color: #fff;
		}
		@media only screen and (max-width: 600px) {
			.ribbon {
				flex-direction: column;
				align-items: center;
			}
			.home-button, .contact-button {
				margin: 10px 0;
			}
		}
	</style>
</head>
<body>
<div class="ribbon">
		<a href="login" class="home-button">Home</a>
		<a href="contactUs.html" class="contact-button">Contact Us</a>
</div>
	<div class="container">
		<form method="POST" action="/contactUs">
			<label for="name">Name:</label>
			<input type="text" id="name" name="name" placeholder="Enter your name" required>
			<label for="age">Age:</label>
			<input type="text" id="age" name="age" placeholder="Enter your Age" required>
			<label for="gender">Gender:</label>
			<select id="gender" name="gender" required>
				<option value="">Select gender</option>
				<option value="male">Male</option>
				<option value="female">Female</option>
				<option value="other">Other</option>
			</select>
			<label for="grade">Grade:</label>
			<input type="text" id="grade" name="grade" placeholder="Enter your Grade" required>
			<input type="submit" value="Submit">
		</form>
	</div>
</body>
</html>












2. I create Backend of the Application Using Python Flask Library, Flsk library is suitable for lightweight application
i have three option Django, Flask and Streamlit library i choose flask

here is My code 

#!/usr/bin/env python
# coding: utf-8

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
def contactUs():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        grade = request.form['grade']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, age, gender, grade) VALUES (%s, %s, %s, %s)",
                    (name, age, gender, grade))
        mysql.connection.commit()
        cur.close()
        
        return 'User information submitted successfully!'
    
    return render_template('contactUs.html')

@app.route('/login', methods=['GET', 'POST'])
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







3. Database- I choose Mysql Database 
first i create adatabase name of test2 then create table name of user in database 

CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL,
      password VARCHAR(255) NOT NULL,
       name VARCHAR(100) NOT NULL,
       age INT NOT NULL,
       gender VARCHAR(10) NOT NULL,
       grade VARCHAR(2) NOT NULL
     );
    
    INSERT INTO users (username, password, name, age, gender, grade)
     VALUES
        ('student1', SHA2('password1', 256), 'John Doe', 18, 'Male', 'A'),
         ('student2', SHA2('password2', 256), 'Jane Smith', 17, 'Female', 'B'),
         ('student3', SHA2('password3', 256), 'Michael Johnson', 16, 'Male', 'A'),
         ('student4', SHA2('password4', 256), 'Emily Davis', 18, 'Female', 'A'),
         ('student5', SHA2('password5', 256), 'David Wilson', 17, 'Male', 'B'),
         ('student6', SHA2('password6', 256), 'Emma Anderson', 16, 'Female', 'B'),
         ('student7', SHA2('password7', 256), 'Daniel Martinez', 17, 'Male', 'A'),
         ('student8', SHA2('password8', 256), 'Olivia Brown', 18, 'Female', 'A'),
         ('student9', SHA2('password9', 256), 'William Taylor', 16, 'Male', 'B'),
         ('student10', SHA2('password10', 256), 'Sophia Thomas', 17, 'Female', 'B');
Query OK, 10 rows affected (0.00 sec)

SHA2 function is used to hash the passwords before storing them in the database.

why we use SHA2:

![3](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/3c68e3c5-e701-49ce-be61-bf330c5e6a1a)


    Password Security: Storing passwords in plain text is highly insecure because if the database is compromised, all passwords would be exposed. To enhance security, passwords should be hashed, which means converting them into irreversible, fixed-length values.

    One-Way Hashing: SHA2 (Secure Hash Algorithm 2) is a cryptographic hash function that performs one-way hashing. It takes an input (in this case, the passwords) and produces a unique fixed-length hash value. The key feature of a cryptographic hash function is that it is computationally infeasible to reverse-engineer the original input from the hash value.
    
    
    Create a folder named templates in the same directory as app.py.

Inside the templates folder, create a file named login.html and add the HTML code for the login form.

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST" action="/login">
        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>




    
    Open a terminal or command prompt, navigate to the directory containing app.py, and run the following command to start the Flask development server:
    
    
    
    ![4](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/75ea017a-33d2-4881-b993-1be51f2ef48e)


Open a web browser and visit http://localhost:5000 to access the home page.

You can then navigate to http://localhost:5000/login to access the login page and test the login and logout functionality.
    



Home Page

![1](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/30bf1e0f-efe1-4501-89bd-67b7501d6387)


Mobile Compatibility of App


![mobile compatiility](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/df90ed22-9739-4a98-903c-89e0f10dea16)


Login Page
![Login Page](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/a1f29d27-187a-4780-982b-8fe0d6406917)



Contact_us


![Contact_us](https://github.com/Mayur96k/Xenon_stack-Round-2/assets/114133429/b272c91a-0021-4497-9664-4ac9909ae7f7)
 If someone enter a data into this it will store in mysql database
 
 
 
 


Source Code


#!/usr/bin/env python
# coding: utf-8

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
def contactUs():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        grade = request.form['grade']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, age, gender, grade) VALUES (%s, %s, %s, %s)",
                    (name, age, gender, grade))
        mysql.connection.commit()
        cur.close()
        
        return 'User information submitted successfully!'
    
    return render_template('contactUs.html')

@app.route('/login', methods=['GET', 'POST'])
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

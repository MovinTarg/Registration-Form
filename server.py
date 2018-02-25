from flask import Flask, render_template, request, redirect, flash
import re

app = Flask(__name__)
app.secret_key = 'movintarg'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/completedForm', methods=['POST'])
def completedForm():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
        return redirect('/')
    elif any(i.isdigit() for i in request.form['first_name']) == True:
        flash("Invalid first name!")
        return redirect('/')
    elif len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
        return redirect('/')
    elif any(i.isdigit() for i in request.form['last_name']) == True:
        flash("Invalid last name!")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Password must contain at least eight characters!")
        return redirect('/')
    elif any(i.isdigit() for i in request.form['password']) != True:
        flash("Password must contain at least 1 number!")
        return redirect('/')
    elif any(i.isupper() for i in request.form['password']) != True:
        flash("Password must contain at least uppercase letter!")
        return redirect('/')
    elif len(request.form['confirm_password']) < 1:
        flash("Confirm password cannot be empty!")
        return redirect('/')
    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords must match!")
        return redirect('/')
    else:
        flash("Registration Complete! Form submitted.")
        return redirect('/')

app.run(debug = True)
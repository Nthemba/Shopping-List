
# views.py

from flask import render_template,request

from app import app

from app import user

@app.route('/')
def index():
	# username = request.form['username']
	# password = request.form['password']
	return render_template("index.html")

@app.route('/signup')
def signup():
	# email = request.form['username']
	# username = request.form['username']
	# password = request.form['password']
	# cPassword = request.form['confirm']
 	return render_template("signup.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")




from flask import Flask, send_from_directory, request, flash, redirect, session
from flask import render_template
from flask_pymongo import PyMongo
import os
import mongodb_query



app = Flask(__name__)
app.secret_key = b'eHk\x8d\xd9\x18\xf1\xd9)#\xaaf\x8aK=<'

app.config["MONGO_URI"] = os.environ['MONGODB_URI']
mongo = PyMongo(app)
#session = False

#login_manager = LoginManager()
#login_manager.init_app(app)




@app.route('/', methods = ['GET','POST'])
def login():
	if request.method == "POST":
		if mongodb_query.user_exist(request.form['username'], request.form['password']):
			session['username'] = request.form['username']
			return redirect('mainpage')
		else:
			return render_template('error_login.html')
	elif request.method == "GET":
		if 'username' in session:
			return render_template('main_info.html')
	return render_template('login_page.html')

@app.route('/mainpage')
def mainpage():
	if request.method == "GET":
		if 'username' in session:
			return render_template('main_info.html')
		else:
			return redirect ('/')


@app.route('/showregistered', methods = ['GET','POST'])
def showregistered():
	if 'username' in session:
		return render_template('main_info.html', users = mongodb_query.showAllUsers())

@app.route('/register', methods = ['GET','POST'])
def register():
	if request.method == "GET":
		if 'username' in session:
			return render_template('main_info.html')
		else:
			return render_template('register_page.html')
	elif request.method == "POST":
		if mongodb_query.create_user(request.form['username'], request.form['password']):
			return redirect ('mainpage')
		else:
			flash("This username is already in use. Please try another one")
			return render_template('register_page.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect ('/')

@app.route('/changepass', methods = ['GET','POST'])
def changepass():
	if request.method == "POST":
		if 'username' in session:
			if request.form['new_password'] == request.form['new_password2']:
				if mongodb_query.change_pass(session['username'], request.form['old_password'], request.form['new_password']):
					flash("Password successfuly canged")
					return render_template('main_info.html')
				else:
					flash("Wrong old password")
					return render_template('changepass_page.html')
			else:
				flash("Passwords should be the same")
				return render_template('changepass_page.html')
	if request.method == "GET":
		if 'username' in session:
			return render_template('changepass_page.html')



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

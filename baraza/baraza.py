import os
import sqlite3

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def landingpage():
	return render_template('home.html')


@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/cases')
def cases():
	return render_template('cases.html')

@app.route('/chiefs')
def chiefs():
	return render_template('chiefs.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')

@app.route('/registerchiefs')
def registerchiefs():
	return render_template('registerchiefs.html')

if __name__ == '__main__':
	app.run(debug=True)
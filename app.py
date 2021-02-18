from flask import Flask,request, redirect, url_for, render_template
import smtplib

from flask_mail import Mail,Message

app = Flask(__name__)

@app.route('/home')
@app.route('/welcome')
@app.route('/')
def home():
    return render_template('home.html')
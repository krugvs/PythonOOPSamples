# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import Column, Integer, String, Boolean
#from sqlalchemy.ext.declarative import declarative_base
from models.user.entity import User
from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route("/")
def hello():
    engine = create_engine('')
    Session = sessionmaker(bind=engine)
    session = Session()
    return render_template('hello.html', users=session.query(User).order_by(User.id))
    

    
    
@app.route('/signupform')
def showSignUp():
    return render_template('signup.html')
    
@app.route('/signup',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    
    # validate the received values
    if _name and _email and _password:
        engine = create_engine('')
        Session = sessionmaker(bind=engine)
        session = Session()
        user = User()
        user.name = _name
        user.email = _email
        user.password = _password
        user.active = True
        user.created = ''#TODO
        user.modified = ''#TODO
        session.add(user)
        session.commit()
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    

    

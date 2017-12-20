# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect
from flask import request, make_response
from flask import session
from flask import flash
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig

# from sqlalchemy.sql import table, column, select, update, insert
# from sqlalchemy import or_, and_
# from sqlalchemy import text

from babel import *
from models import db
import forms

import urllib, json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route('/', methods = ['GET','POST'])
def index():
    form = forms.SearchForm()
    data = []
    if request.method == 'POST':
        q = form.text.data
        url = "http://192.168.1.112:5000/brute?query="+q
        url = url.replace(" ", "%20")
        response = urllib.urlopen(url)
        my_data = json.loads(response.read())
        data = my_data["results"]

        # my_data = my_data["results"]
        # for d in my_data:
        #     print d["similarity"], d["document"]["NOMBRE"]
        
        # for value in data:
        #     print value
    return render_template('index.html', form = form, data = data)

@app.route('/general', methods = ['GET','POST'])
def general():
    return render_template('general.html')

@app.route('/avanzado', methods = ['GET','POST'])
def avanzado():
    form = forms.SearchForm()
    data = []
    cities = []
    if request.method == 'POST':
        q = form.text.data
        url = "http://192.168.1.112:5000/brute?query="+q
        url = url.replace(" ", "%20")
        response = urllib.urlopen(url)
        my_data = json.loads(response.read())
        cities = my_data["entities"]
        data = my_data["results"]
    return render_template('avanzado.html', form = form, data = data, cities = cities)

if __name__ == '__main__':
    csrf.init_app(app)
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    app.run(host='127.0.0.1', port=5000, threaded=True)

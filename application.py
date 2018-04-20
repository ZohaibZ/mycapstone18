from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table
from application import db, application
from application.models import *
from application.forms import *
import random

application.secret_key = 'Capstone2018'

@application.route('/index.html')
@application.route('/')
def index():
    engine = create_engine('mysql+pymysql://Capstone2018:capstonehelp@capstone2018.cffs7lx8bqq2.us-east-1.rds.amazonaws.com:3306/Capstone2018', convert_unicode=True)
    connection = engine.connect()
    X = True

    while X:
        scan = random.randint(0, 1)
        if scan == 1:
            print('SCANNING')
            return render_template('blank-page.html')
        else:
            print('NOT SCANNING')
            return render_template('index.html')

    return render_template('index.html')

@application.route('/pages/<folder>/<page>')
def pages(folder,page):
    X = 'pages/{}/{}'.format(folder,page)
    print(X)
    return render_template(X)

if __name__== '__main__':
# here is starting of the development HTTP server
    application.run(debug=True)

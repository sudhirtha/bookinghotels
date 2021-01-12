from flask import Flask
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='postgres+psycopg2://{}:{}@{}/{}'.format('zhdiznduxcemmt','85325826bd2a1f8780d4ec4e3082b615a2fe1f0eac82929e0a5daa60710eb8f8','ec2-52-204-113-104.compute-1.amazonaws.com','d5m6rkbonukbu6')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1238sadh1234390823kjhdJKA*(@E$^$'

db=SQLAlchemy(app)

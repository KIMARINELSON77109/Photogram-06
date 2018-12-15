from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


UPLOAD_FOLDER = './app/static/uploads'
TOKEN_SECRET = 'Thisissecret'

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://btyoeetywrnblt:243fead832fc46e25c1d0076e811249e52c75e2ae831c724882cd05349cff004@ec2-54-227-249-201.compute-1.amazonaws.com:5432/d6vovl10vtdlie"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
csrf = CSRFProtect(app)

db = SQLAlchemy(app)


app.config.from_object(__name__)
filefolder = app.config['UPLOAD_FOLDER']
token_key = app.config['TOKEN_SECRET']
from app import views
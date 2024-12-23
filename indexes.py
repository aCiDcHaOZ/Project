from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

#Zorgen dat het standaard pad zoals c:\blah in windows of /blah/ in linux opgehaald
#kan worden. Hierdoor kan er makkelijker naar bestanden worden gerefereerd.
basedir = os.path.abspath(os.path.dirname(__file__) 

#Start een nieuwe Flask-applicatie
app = Flask(__name__)

#Zoek in de basisdirectory naar het bestand op het einde van de regel hieronder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bungalow.db')
#Zet debug-modus aan/uit voor bewerkingen in de database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Koppel de database aan de Flask-applicatie
db = SQLAlchemy(app)

#Nieuwe tabellen aanmaken, dit wordt gedaan door middel van Objecten in python ...

#Tabel gebruikers
class Gebruikers(db.model):
    idnr = db.Column(db.Integer,primary_key=True)
    naam = db.Column(db.Text)
    email = db.Column(db.Text)
    telnr = db.Column(db.Text)

def __init__(self,naam,leeftijd):
    self.id = idnr
    self.naam = naam
    self.email = email
    self.telnr = telnr
    


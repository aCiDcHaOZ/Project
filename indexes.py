from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os

#Zorgen dat het standaard pad zoals c:\blah in windows of /blah/ in linux opgehaald
#kan worden. Hierdoor kan er makkelijker naar bestanden worden gerefereerd.
basedir = os.path.abspath(os.path.dirname(__file__))

#Start een nieuwe Flask-applicatie
app = Flask(__name__)

#Zoek in de basisdirectory naar het bestand op het einde van de regel hieronder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bungalow.db')
#Zet debug-modus aan/uit voor bewerkingen in de database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Koppel de database aan de Flask-applicatie
db = SQLAlchemy(app)

#Als er een beroep wordt gedaan op een tabel in de DB die niet bestaat,
#Maak deze dan.
@app.before_request
def create_tables():
    db.create_all()

#Route naar de hoofdpagina
@app.route("/")
def index():
    return render_template("/templates/voorpagina.html")

#Route naar prijslijst
@app.route("/prijslijst")
def Prijslijst():
    return render_template("/templates/Prijslijst.html")

#Route naar prijslijst
@app.route("/prijslijst")
def Prijslijst():
    return render_template("/templates/Prijslijst.html")

#Nieuwe tabellen aanmaken, dit wordt gedaan door middel van Objecten in python ...

#Tabel gebruikers
class Gebruikers(db.Model):
    idnr = db.Column(db.Integer,primary_key=True)
    naam = db.Column(db.Text)
    email = db.Column(db.Text)
    telnr = db.Column(db.Text)

def __init__(self,naam,leeftijd):
    self.id = idnr
    self.naam = naam
    self.email = email
    self.telnr = telnr


#Bij error 404, laat 404.html zien
@app.errorhandler(404)
def pagina_niet_gevonden(e):
    return render_template("404.html"), 404


#Als de app niet vanaf extern opgeroepen wordt, starten.
if __name__ == "__main__":
    app.run(debug=True)
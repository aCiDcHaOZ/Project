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
@app.route("/overons")
def Prijslijst():
    return render_template("/templates/overons.html")


#Als de app niet vanaf extern opgeroepen wordt, starten.
if __name__ == "__main__":
    app.run(debug=True)
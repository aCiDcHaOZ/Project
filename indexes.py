from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


#Importeer de onderstaande klassen van het Py-bestand Forms om met formulieren 
#te kunnen werken.
from forms import RegForm

#Importeer de onderstaande klassen van het Py-bestand dbmodel om met de database
#te kunnen werken.
from dbmodel import db, Klant, Reis, Boeking

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

app.config['SECRET_KEY'] = 'your_secret_key'

#Als er een beroep wordt gedaan op een tabel in de DB die niet bestaat,
#Maak deze dan aan.
@app.before_request
def create_tables():
    db.create_all()

#Route naar de hoofdpagina
@app.route('/')
def index():
    return render_template('voorpagina.html')

#Route naar prijslijst
@app.route('/prijslijst')
def PrijsLijst():
    return render_template('Prijslijst.html')

#Route naar overons
@app.route('/overons')
def OverOns():
    return render_template('overons.html')

#Route naar Boekingsformulier
@app.route('/boekingsformulier')
def BoekingsFormulier():
    return render_template('Boekingsformulier.html')

#Route naar Registreren
@app.route('/registreren')
def Registreren():
    form = RegForm()
    if form.validate_on_submit():
        klant = klant(naam=form.naam.data, email=form.email.data, telefoon=form.telefoon.data)
        db.session.add(klant)
        db.session.commit()
        flash('Klant succesvol toegevoegd!', 'success')
        return redirect(url_for('klanten'))
    return render_template('registreren.html', form=form)

#Route naar Faciliteiten
@app.route('/faciliteiten')
def Faciliteiten():
    return render_template('Faciliteiten.html')

#Route naar Fotogalerij
@app.route('/fotogalerij')
def FotoGalerij():
    return render_template('fotogalerij.html')

#Route naar registratieformulier voor lan
@app.route('/reglan')
def RegLan():
    return render_template('regform_lan.html')

#Route voor foutmelding 404
@app.errorhandler(404)
def pagina_niet_gevonden(e):
    return render_template('404.html'), 404


#Als de app niet vanaf extern opgeroepen wordt, starten.
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt #Versleuteling
from flask_login import LoginManager
import os
# Importeer de onderstaande klassen van het Py-bestand Forms om met formulieren 
# te kunnen werken.
from Formulieren import KlantForm, LanForm, LoginForm, BoekingForm
# Importeer de onderstaande klassen van het Py-bestand dbmodel om met de database
# te kunnen werken.
from dbmodel import db, Klant, Lanparty, Reis, Boeking
 
# Zorgen dat het standaard pad zoals c:\blah in windows of /blah/ in linux opgehaald
# kan worden. Hierdoor kan er makkelijker naar bestanden worden gerefereerd.
basedir = os.path.abspath(os.path.dirname(__file__))
 
# Start een nieuwe Flask-applicatie
app = Flask(__name__)
 
# Configuraties
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bungalow.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
 
# Koppel de database aan de Flask-applicatie
db.init_app(app)

# Initalizatie van Bcrypt, koppeling aan de python app. 
# Nodig voor hash, niet degene uit de coffeeshop.
bcrypt = Bcrypt(app)

#Initializatie van login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Iemand wordt naar de route login verwezen als een pagina dat vereist.
login_manager.login_message_category = 'info' # Notificatie als iemand oningelogd een beveiligde pagina bezoekt.
 
# Maak tabellen indien ze niet bestaan
@app.before_request
def create_tables():
    db.create_all()
 
# Route naar de hoofdpagina
@app.route('/')
def index():
    return render_template('voorpagina.html')
 
# Route naar prijslijst
@app.route('/prijslijst')
def PrijsLijst():
    return render_template('Prijslijst.html')
 
# Route naar overons
@app.route('/overons')
def OverOns():
    return render_template('overons.html')
 
# Route naar boekingsformulier
@app.route('/boekingsformulier', methods=['GET', 'POST'])
def BoekingsFormulier():
    form = BoekingForm()
    if form.validate_on_submit():
        #Strings defineren adhv pointers in de HTML
        boeking = Boeking(
            name=form.username.data, 
            email=form.email.data, 
            phone=form.phone.data, 
            arrival=form.arrival.data, 
            departure=form.departure.data, 
            adults=form.adults.data, 
            special=form.special.data, 
            payment=form.payment.data, 
            promo=form.promo.data)
    return render_template('Boekingsformulier.html', form=form)
 
# Route naar registreren
@app.route('/registreren', methods=['GET', 'POST'])
def Registreren():
    form = KlantForm()
    if form.validate_on_submit():
        klant = Klant(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(klant)
        db.session.commit()
        flash('Klant succesvol toegevoegd!', 'success')
        return redirect(url_for('index'))
    return render_template('registreren.html', form=form)


# Een pagina om LAN-party's te registreren
@app.route('/reglan', methods=['GET', 'POST'])
def lan_toevoegen():
    form = LanForm()
    if form.validate_on_submit():
        lanparty = Lanparty(naam=form.username.data, email=form.email.data, password=form.telnr.data, datum=form.datum.data, gasten=form.gasten.data, verzoeken=form.verzoeken.data)
        db.session.add(lanparty)
        db.session.commit()
        flash('Reis succesvol toegevoegd!', 'success')
        return redirect(url_for('index'))
    return render_template('regform_lan.html', form=form, actie='Toevoegen')

# Route voor de inlogpagina
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Maak een nieuw formulier aan vanuit de klasse LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        # Hieronder worden de ingevulde gegevens verwerkt
        email = form.username.data
        password = form.password.data
        # Zijn de ingevoerde gegevens correct? Ga dan weer terug naar Home
        return redirect(url_for('home'))
    return render_template('login.html', form=form)



# Route naar faciliteiten
@app.route('/faciliteiten')
def Faciliteiten():
    return render_template('Faciliteiten.html')
 
# Route naar fotogalerij
@app.route('/fotogalerij')
def FotoGalerij():
    return render_template('fotogalerij.html')
 

# Foutafhandeling 404
@app.errorhandler(404)
def pagina_niet_gevonden(e):
    return render_template('404.html'), 404
 
# Start de applicatie
if __name__ == "__main__":
    app.run(debug=True)
from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from forms import KlantForm, LoginForm, LanForm
from dbmodel import Klant
from flask_login import login_user, current_user, logout_user, login_required

# Route naar de hoofdpagina
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html', title='Home')
 
# Route naar prijslijst
@app.route('/prijslijst')
def PrijsLijst():
    return render_template('Prijslijst.html')
 
# Route naar overons
@app.route('/overons')
def OverOns():
    return render_template('overons.html')

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Klant.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('user'))
        else:
            flash('Inloggen mislukt. Controleer je email en wachtwoord.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/user")
@login_required
def user():
    return render_template('user.html', title='Account')

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

# Een pagina om LAN-party's te registreren
@app.route('/reglan', methods=['GET', 'POST'])
@login_required
def lan_toevoegen():
    form = LanForm()
    if form.validate_on_submit():
        lanparty = LanForm(naam=form.username.data, email=form.email.data, password=form.telnr.data, datum=form.datum.data, gasten=form.gasten.data, verzoeken=form.verzoeken.data)
        db.session.add(lanparty)
        db.session.commit()
        flash('Reis succesvol toegevoegd!', 'success')
        return redirect(url_for('index'))
    return render_template('regform_lan.html', form=form, actie='Toevoegen')

# Route naar boekingsformulier
@app.route('/boekingsformulier', methods=['GET', 'POST'])
@login_required
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
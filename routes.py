from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from Formulieren import *
from dbmodel import KlantTabel, LanTabel, BoekingTabel, BungalowTabel
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/home')
@app.route('/')
def home():
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistratieFormulier()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        Klanttabel = KlantTabel(
            username=form.username.data, 
            email=form.email.data, 
            password=hashed_password)
        db.session.add(Klanttabel)
        db.session.commit()
        flash('Klant succesvol toegevoegd!', 'success')
        return redirect(url_for('home'))
    return render_template('registreren.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginFormulier()
    if form.validate_on_submit():
        user = KlantTabel.query.filter_by(email=form.email.data).first()
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
@app.route('/lanp/reg', methods=['GET', 'POST'])
@login_required
def lan_toevoegen():
    # Maak een nieuw formulier (form) van het type LanFormulier
    form = LanFormulier()
    if form.validate_on_submit():
        lanformulier = LanTabel(
            lannaam=form.lannaam.data, 
            organisator=form.organisator.data, 
            email=form.email.data, 
            datum=form.datum.data, 
            aantalstoelen=form.aantalstoelen.data, 
            opmerking=form.opmerking.data)
        db.session.add(lanformulier)
        db.session.commit()
        flash('LANparty succesvol toegevoegd!', 'success')
        return redirect(url_for('home'))
    return render_template('regform_lan.html', form=form, actie='Toevoegen')

# Route naar boekingsformulier
@app.route('/boeking/toevoegen', methods=['GET', 'POST'])
@login_required
def boeking_toevoegen():
    form = BoekingFormulier()
    bungalows = BungalowTabel.query.all()
    print(bungalows)
    if form.validate_on_submit():
        #Strings defineren adhv pointers in de HTML
        boekingformulier = BoekingTabel(
            username=form.username.data, 
            email=form.email.data, 
            phone=form.phone.data,
            bungalow_id=form.bungalow.data,
            arrival=form.arrival.data,
            duration=form.duration.data)
        print(boekingformulier)
        db.session.add(boekingformulier)
        db.session.commit()
        print("Boeking is succesvol")
        flash('Boeking succesvol toegevoegd!', 'success')
        return redirect(url_for('home'))
    return render_template('Boekingsformulier.html', form=form, bungalows=bungalows)

#@app.route('/lanparties')
#def lanparties():
#    lanparties = Lanparties.query.all()
#    return render_template('reis.html', reizen=reizen)

@app.route('/add_registration', methods=['POST'])
@login_required
def add_registration():
    form = LanFormulier()
    if form.validate_on_submit():
        lan_party_dates = {
            "15-februari": "15 februari",
            "22-februari": "22 februari",
            "1-maart": "1 maart"
        }
        selected_lan_party = form.lan_party.data
        datum = lan_party_dates.get(selected_lan_party, "")

        lan_registration = LanTabel(
            lannaam="LAN Party",
            organisator=form.organisator.data,
            email=form.email.data,
            datum=datum,
            aantalstoelen=form.aantalstoelen.data,
            opmerking=form.opmerking.data
        )
        db.session.add(lan_registration)
        db.session.commit()
        flash("Registratie succesvol toegevoegd!", "success")
        return redirect(url_for('home'))
    flash("Er is een fout opgetreden bij het invullen van het formulier.", "danger")
    return render_template('regform_lan.html', form=form)


@app.route('/admin', methods=['GET', 'POST', 'DELETE'])
def klanten():
    users = KlantTabel.query.all()
    parties = LanTabel.query.all()
    boekingen = BoekingTabel.query.all()    
    lodges = BungalowTabel.query.all()
    print(boekingen) 
    return render_template('admin.html', users=users, parties=parties, boekingen=boekingen, lodges=lodges)


@app.route('/lanp/verwijder/<int:id>', methods=['GET', 'POST', 'DELETE'])
def del_lanp(id):
    record = LanTabel.query.get(id)
    if record is None:
        flash('Record niet gevonden.', 'error')
        return redirect("/admin", code=302)
    print(record)
    db.session.delete(record)
    db.session.commit()
    flash('Record succesvol verwijderd.', 'success')
    return redirect("/admin", code=302)

# UPDATE LANPARTY TEST
@app.route('/lanp/update/<int:id>', methods=['GET', 'POST'])
def upd_lanp(id):
    party = LanTabel.query.get(id)
    form=LanFormulier(obj=party)
    print(party)
    if form.validate_on_submit():
        print("Valide!")
        party.organisator = form.organisator.data
        party.email = form.email.data
        party.aantalstoelen = form.aantalstoelen.data
        party.opmerking = form.opmerking.data
        db.session.commit()
        flash('Lan-Party succesvol bijgewerkt!', 'success')
        return redirect("/admin", code=302)
    return render_template('regform_lan.html', form=form, actie='Wijzigen')   



# Klant updaten
@app.route('/klant/update/<int:id>', methods=['GET', 'POST'])
def upd_user(id):
    klant = KlantTabel.query.get_or_404(id)
    form = RegistratieFormulier(obj=klant)
    print(klant)

    if form.validate_on_submit():
        print("Valide!")
        klant.username = form.username.data
        klant.email = form.email.data
        db.session.commit()
        flash('Lan-Party succesvol bijgewerkt!', 'success')
        return redirect("/admin", code=302)
    return render_template('registreren.html', form=form, actie='Wijzigen')




@app.route('/boekp/verwijder/<int:id>', methods=['GET', 'POST', 'DELETE'])
def del_boek(id):
    record = BoekingTabel.query.get(id)
    if record is None:
        flash('Record niet gevonden.', 'error')
        return redirect("/admin", code=302)
    print(record)
    db.session.delete(record)
    db.session.commit()
    flash('Record succesvol verwijderd.', 'success')
    return redirect("/admin", code=302)


@app.route('/klant/verwijder/<int:id>', methods=['GET', 'POST', 'DELETE'])
def del_user(id):
    record = KlantTabel.query.get(id)
    if record is None:
        flash('Record niet gevonden.', 'error')
        return redirect("/admin", code=302)
    print(record)
    db.session.delete(record)
    db.session.commit()
    flash('Record succesvol verwijderd.', 'success')
    return redirect("/admin", code=302)

@app.route('/lodge/aanmaken', methods=['GET', 'POST'])
@login_required
def bungalow_toevoegen():
    # Maak een nieuw formulier (form) van het type LanFormulier
    form = BungalowFormulier()
    if form.validate_on_submit():
        form = BungalowTabel(
            bnaam = form.bnaam.data,
            adrescode = form.adrescode.data)
        db.session.add(form)
        db.session.commit()
        flash('Bungalow succesvol toegevoegd!', 'success')
        return redirect(url_for('home'))
    return render_template('/bungalow/aanmaken.html', form=form, actie='Toevoegen')

@app.route('/lodge/verwijder/<int:id>', methods=['GET', 'POST', 'DELETE'])
def bungalow_verwijderen(id):
    record = BungalowTabel.query.get(id)
    if record is None:
        flash('Record niet gevonden.', 'error')
        return redirect("/admin", code=302)
    print(record)
    db.session.delete(record)
    db.session.commit()
    flash('Record succesvol verwijderd.', 'success')
    return redirect("/admin", code=302)

# Klant updaten
@app.route('/lodge/update/<int:id>', methods=['GET', 'POST'])
def update_bungalow(id):
    bungalow = BungalowTabel.query.get_or_404(id)
    form = BungalowFormulier(obj=bungalow)
    print(bungalow)

    if form.validate_on_submit():
        print("Valide!")
        bungalow.bnaam = form.bnaam.data
        bungalow.adrescode = form.adrescode.data
        db.session.commit()
        flash('Bungalow succesvol bijgewerkt!', 'success')
        return redirect("/admin", code=302)
    return render_template('/bungalow/aanmaken.html', form=form, actie='Wijzigen')

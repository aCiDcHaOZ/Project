from flask import Flask, render_template, redirect, url_for, flash,request
from flask_sqlalchemy import SQLAlchemy
from Formulieren import KlantForm, ReisForm, BoekingForm
from models import db, Klant, Reis, Boeking

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reis.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/klanten', methods=['GET', 'POST'])
def klanten():
    klanten = Klant.query.all()
    return render_template('klant.html', klanten=klanten)

@app.route('/klant/toevoegen', methods=['GET', 'POST'])
def klant_toevoegen():
    form = KlantForm()
    if form.validate_on_submit():
        klant = Klant(naam=form.naam.data, email=form.email.data)
        db.session.add(klant)
        db.session.commit()
        flash('Klant succesvol toegevoegd!', 'success')
        return redirect(url_for('klanten'))
    return render_template('klant_form.html', form=form)

@app.route('/klant/<int:id>/wijzigen', methods=['GET', 'POST'])
def klant_wijzigen(id):
    klant = Klant.query.get_or_404(id)
    form = KlantForm(obj=klant)
    if form.validate_on_submit():
        klant.naam = form.naam.data
        klant.email = form.email.data
        db.session.commit()
        flash('Klant succesvol bijgewerkt!', 'success')
        return redirect(url_for('klanten'))
    return render_template('klant_form.html', form=form, actie='Wijzigen')


@app.route('/reizen')
def reizen():
    reizen = Reis.query.all()
    return render_template('reis.html', reizen=reizen)


@app.route('/reis/toevoegen', methods=['GET', 'POST'])
def reis_toevoegen():
    form = ReisForm()
    if form.validate_on_submit():
        reis = Reis(bestemming=form.bestemming.data, prijs=form.prijs.data)
        db.session.add(reis)
        db.session.commit()
        flash('Reis succesvol toegevoegd!', 'success')
        return redirect(url_for('reizen'))
    return render_template('reis_form.html', form=form, actie='Toevoegen')

@app.route('/reis/<int:id>/wijzigen', methods=['GET', 'POST'])
def reis_wijzigen(id):
    reis = Reis.query.get_or_404(id)
    form = ReisForm(obj=reis)
    if form.validate_on_submit():
        reis.bestemming = form.bestemming.data
        reis.prijs = form.prijs.data
        db.session.commit()
        flash('Reis succesvol bijgewerkt!', 'success')
        return redirect(url_for('reizen'))
    return render_template('reis_form.html', form=form, actie='Wijzigen')


@app.route('/boekingen')
def boekingen():
    boekingen = Boeking.query.all()
    return render_template('boeking.html', boekingen=boekingen)


@app.route('/boeking/toevoegen', methods=['GET', 'POST'])
def boeking_toevoegen():
    form = BoekingForm()
    form.klant.choices = [(k.id, k.naam) for k in Klant.query.all()]
    form.reis.choices = [(r.id, r.bestemming) for r in Reis.query.all()]
    if form.validate_on_submit():
        boeking = Boeking(klant_id=form.klant.data, reis_id=form.reis.data)
        db.session.add(boeking)
        db.session.commit()
        flash('Boeking succesvol toegevoegd!', 'success')
        return redirect(url_for('boekingen'))
    return render_template('boeking_form.html', form=form)

@app.route('/boeking/wijzigen/<int:boeking_id>', methods=['GET', 'POST'])
def boeking_wijzigen(boeking_id):
    boeking = Boeking.query.get_or_404(boeking_id)
    form = BoekingForm(obj=boeking)  # Vul formulier met bestaande gegevens

    # Vul de keuzelijsten opnieuw in, zodat de juiste opties beschikbaar zijn
    form.klant.choices = [(k.id, f"{k.naam} ({k.email})") for k in Klant.query.all()]
    form.reis.choices = [(r.id, f"{r.bestemming} - €{r.prijs}") for r in Reis.query.all()]

    # Standaard geselecteerde waarden voor klant en reis instellen
    form.klant.data = boeking.klant_id
    form.reis.data = boeking.reis_id

    if form.validate_on_submit():
        boeking.klant_id = form.klant.data
        boeking.reis_id = form.reis.data
        db.session.commit()
        flash('Boeking is succesvol bijgewerkt!', 'success')
        return redirect(url_for('boekingen'))

    return render_template('boeking_form.html', form=form, actie="Boeking Wijzigen")

@app.errorhandler(404)
def pagina_niet_gevonden(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

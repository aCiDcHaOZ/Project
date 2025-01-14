from app import db, login_manager
from flask_login import UserMixin
import logging

# Config logging for debugging
logging.basicConfig(level=logging.DEBUG)

@login_manager.user_loader
def load_user(user_id):
    return KlantTabel.query.get(int(user_id))

class LanTabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lannaam = db.Column(db.String(80), nullable=False)
    organisator_id = db.Column(db.Integer, db.ForeignKey('klanttabel.id'), nullable=False)  # Relatie naar KlantTabel
    organisator = db.relationship('KlantTabel', backref=db.backref('lans', lazy=True))
    email = db.Column(db.String(120), nullable=False)
    datum = db.Column(db.String(20), nullable=False)
    aantalstoelen = db.Column(db.Integer, nullable=False)
    opmerking = db.Column(db.String(120))

class BoekingTabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    arrival = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Aangepast naar Integer
    adults = db.Column(db.Integer, nullable=False)  # Aangepast naar Integer
    special = db.Column(db.String(120))
    payment = db.Column(db.String(80), nullable=False)
    promo = db.Column(db.String(80))

class KlantTabel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Route voor het verwerken van een formulier
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Log formulierdata
        logging.debug(f"Formulierdata ontvangen: {request.form}")

        # Validatie van vereiste velden
        required_fields = ['username', 'email', 'phone', 'arrival', 'duration', 'adults', 'payment', 'promo']
        for field in required_fields:
            if field not in request.form or not request.form[field]:
                return jsonify({'error': f'Veld {field} is verplicht'}), 400

        # Maak een nieuwe boeking
        boeking = BoekingTabel(
            username=request.form['username'],
            email=request.form['email'],
            phone=request.form['phone'],
            arrival=request.form['arrival'],
            duration=int(request.form['duration']),
            adults=int(request.form['adults']),
            special=request.form.get('special', ''),  # Optioneel veld
            payment=request.form['payment'],
            promo=request.form['promo']
        )

        # Opslaan in de database
        db.session.add(boeking)
        db.session.commit()
        return jsonify({'success': 'Boeking succesvol opgeslagen'}), 200

    except Exception as e:
        db.session.rollback()
        logging.error(f"Fout tijdens het verwerken: {str(e)}")
        return jsonify({'error': f"Er is een fout opgetreden: {str(e)}"}), 500

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Klant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Lanparty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telnr = db.Column(db.String(20), nullable=False)
    datum = db.Column(db.String(20), nullable=False)
    gasten = db.Column(db.Integer, nullable=False)
    verzoeken = db.Column(db.String(120))


class Reis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bestemming = db.Column(db.String(120), nullable=False)
    prijs = db.Column(db.Numeric(10, 2), nullable=False)  # Decimaal type met 2 cijfers achter de komma

class Boeking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    klant_id = db.Column(db.Integer, db.ForeignKey('klant.id'), nullable=False)
    reis_id = db.Column(db.Integer, db.ForeignKey('reis.id'), nullable=False)

#Defineer de relaties tussen verschillende tabellen in de database.
#lazy=true betekent dat de gerelateerde gegevens pas worden opgehaald als ze nodig zijn.
    klant = db.relationship('Klant', backref=db.backref('boekingen', lazy=True))
    reis = db.relationship('Reis', backref=db.backref('boekingen', lazy=True))
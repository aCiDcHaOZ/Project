from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Klant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

class Reis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bestemming = db.Column(db.String(120), nullable=False)
    prijs = db.Column(db.Numeric(10, 2), nullable=False)  # Decimaal type met 2 cijfers achter de komma

class Boeking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    klant_id = db.Column(db.Integer, db.ForeignKey('klant.id'), nullable=False)
    reis_id = db.Column(db.Integer, db.ForeignKey('reis.id'), nullable=False)


    klant = db.relationship('Klant', backref=db.backref('boekingen', lazy=True))
    reis = db.relationship('Reis', backref=db.backref('boekingen', lazy=True))
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return KlantTabel.query.get(int(user_id))

class LanTabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lannaam = db.Column(db.String(80), nullable=False)
    organisator = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    datum = db.Column(db.String(20), nullable=False)
    aantalstoelen = db.Column(db.Integer, nullable=False)
    opmerking = db.Column(db.String(120))

class BungalowTabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bnaam = db.Column(db.String(80), nullable=False)
    adrescode = db.Column(db.String(80), nullable=False)


class BoekingTabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    bungalow_id = db.Column(db.Integer, db.ForeignKey('bungalow_tabel.id'), nullable=False)
    arrival = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.String(80), nullable=False)

    bungalow_tabel = db.relationship('BungalowTabel', backref=db.backref('boekingen'), lazy=True)


class KlantTabel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)


    # Projectie van een object binnen de functie, niet boeiend.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



#    id = db.Column(db.Integer, primary_key=True)
#    klant_id = db.Column(db.Integer, db.ForeignKey('klant.id'), nullable=False)
#    reis_id = db.Column(db.Integer, db.ForeignKey('reis.id'), nullable=False)

#Defineer de relaties tussen verschillende tabellen in de database.
#lazy=true betekent dat de gerelateerde gegevens pas worden opgehaald als ze nodig zijn.
#    klant = db.relationship('Klant', backref=db.backref('boekingen', lazy=True))
#    reis = db.relationship('Reis', backref=db.backref('boekingen', lazy=True))


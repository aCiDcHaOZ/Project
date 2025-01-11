from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Email

class KlantForm(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

class LanForm(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telnr = StringField('Telefoonnummer', validators=[DataRequired()])
    datum = StringField('Datum', validators=[DataRequired()])
    gasten = StringField('Aantal gasten', validators=[DataRequired()])
    verzoeken = StringField('Verzoeken')    
    submit = SubmitField('Toevoegen')

class BoekingForm(FlaskForm):
    klant = SelectField('Klant', coerce=int)
    reis = SelectField('Reis', coerce=int)
    submit = SubmitField('Boek')

class LoginForm(FlaskForm):
    email = StringField('Email adres', validators=[DataRequired(), Email()])
    #Hieronder zou een passwordfield moeten zijn, werkt echter niet. voor nu stringfield
    password = StringField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('inloggen')

class boekingForm(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Telefoonnummer', validators=[DataRequired()])
    arrival = DateField('AankomstDatum', validators=[DataRequired()])
    departure = DateField('VertrekDatum', validators=[DataRequired()])
    adults = StringField('Volwassenen', validators=[DataRequired()])
    special = StringField('SpecialeWensen')
    payment = StringField('Payment', validators=[DataRequired()])
    promo = StringField('PromoCode')
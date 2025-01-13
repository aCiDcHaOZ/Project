from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from dbmodel import KlantTabel

class RegistratieFormulier(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    confirm_password = PasswordField('Bevestig wachtwoord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registreer')

    #Controleren of gebruikersnaam al in gebruik is
    def validate_username(self, username):
        user = KlantTabel.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Deze gebruikersnaam is al bezet.')

    #Controleren of email adres al in gebruik is
    def validate_email(self, email):
        user = KlantTabel.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Deze email is al geregistreerd.')

class LanFormulier(FlaskForm):
    lannaam = StringField('Naam Lanparty', validators=[DataRequired()])
    organisator = StringField('Naam', validators=[DataRequired()]) 
    email = StringField('Email', validators=[DataRequired(), Email()])
    datum = DateField('Datum', validators=[DataRequired()])
    aantalstoelen = StringField('Aantal plekken', validators=[DataRequired()])
    opmerking = StringField('Opmerking')    
    submit = SubmitField('Toevoegen')

class LoginFormulier(FlaskForm):
    email = StringField('Email adres', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('inloggen')

class BoekingFormulier(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Telefoonnummer', validators=[DataRequired()])
    arrival = DateField('AankomstDatum', validators=[DataRequired()])
    departure = DateField('VertrekDatum', validators=[DataRequired()])
    adults = StringField('Volwassenen', validators=[DataRequired()])
    special = StringField('SpecialeWensen')
    payment = StringField('Payment', validators=[DataRequired()])
    promo = StringField('PromoCode')
    submit = SubmitField('Boek')


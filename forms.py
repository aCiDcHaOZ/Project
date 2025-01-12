from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from dbmodel import Klant

class KlantForm(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    confirm_password = PasswordField('Bevestig wachtwoord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registreer')

    #Controleren of gebruikersnaam al in gebruik is
    def validate_username(self, username):
        user = Klant.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Deze gebruikersnaam is al bezet.')

    #Controleren of email adres al in gebruik is
    def validate_email(self, email):
        user = Klant.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Deze email is al geregistreerd.')

class LanForm(FlaskForm):
    username = StringField('Naam', validators=[DataRequired()])
    password = StringField('Wachtwoord', validators=[DataRequired(), Email()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telnr = StringField('Telefoonnummer', validators=[DataRequired()])
    datum = StringField('Datum', validators=[DataRequired()])
    gasten = StringField('Aantal gasten', validators=[DataRequired()])
    verzoeken = StringField('Verzoeken')    
    submit = SubmitField('Toevoegen')

class LoginForm(FlaskForm):
    email = StringField('Email adres', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('inloggen')

class BoekingForm(FlaskForm):
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
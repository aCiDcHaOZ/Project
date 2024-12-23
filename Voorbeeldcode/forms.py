from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class KlantForm(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Toevoegen')

class ReisForm(FlaskForm):
    bestemming = StringField('Bestemming', validators=[DataRequired()])
    prijs = FloatField('Prijs', validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

class BoekingForm(FlaskForm):
    klant = SelectField('Klant', coerce=int)
    reis = SelectField('Reis', coerce=int)
    submit = SubmitField('Boek')

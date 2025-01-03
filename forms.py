from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class KlantForm(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Toevoegen')

class LanForm(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
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

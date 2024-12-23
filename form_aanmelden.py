from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class InfoForm(FlaskForm):
    instrument = StringField('Welk instrument wil je graag bespelen?', validators=[DataRequired()])
    submit = SubmitField('Verzend')

@app.route("/", methods=['GET', 'POST'])  # Route defineren voor het formulier
def index():
    name = None  # Initialiseer instrument als None
    phone = None
    email = None
    gender = None
    form = InfoForm()  # Maak een object van het type InfoForm
    if form.validate_on_submit():
        instrument = form.instrument.data
        form.instrument.data = ''  # Reset het invoerveld
    return render_template('registreren.html', form=form, instrument=instrument, phone=phone, email=email, name=name, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)


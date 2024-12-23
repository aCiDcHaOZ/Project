from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class InfoForm(FlaskForm):
    instrument = StringField('Welk instrument wil je graag bespelen?')
    submit = SubmitField('Verzend')

@app.route("/", methods=['GET', 'POST']) #Route defineren voor het formulier
def index():
    instrument = False 
    form = InfoForm() #maak een object van het type InfoForm()
    if form.validate_on_submit():
        instrument = form.instrument.data
        form.instrument.data = ''
        return render_template('/templates/registreren.html', form=form, instrument=instrument)
    
if __name__ == '__main__':
    app.run(debug=True)


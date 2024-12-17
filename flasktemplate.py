#importeren uit de flask library: flask en render_template
from flask import Flask, render_template
from flask_wtf import FlaskForm #importeer ondersteuning voor formulieren
from wtforms import StringField, SubmitField #uit form ondersteuning
#Een nieuwe instantie aanmaken
app = Flask(__name__)

@app.route("/") #als iemand gaat naar www.site.nl/
def index(): #defineer een nieuwe functie
    return render_template("basic.html") #de template (sjabloon) basic.html

@app.route("/templates/overons") #als iemand gaat naar site.nl/overons
def overons(): #defineer een nieuwe functie
    return render_template("overons.html")

if __name__ == "__main__": #Controle of het script elders opgeroepen wordt. Zo niet: Run code
    app.run(debug=True) #Start de webserver met gedetailleerde foutrapportering
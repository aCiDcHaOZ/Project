from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# Start een nieuwe Flask-applicatie en configureer
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bungalow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Koppel de database aan de Flask-applicatie
db = SQLAlchemy(app)

# Initalizatie van Bcrypt, koppeling aan de python app. 
# Nodig voor hash, niet degene uit de coffeeshop.
bcrypt = Bcrypt(app)

#Initializatie van login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Iemand wordt naar de route login verwezen als een pagina dat vereist.
login_manager.login_message_category = 'info' # Notificatie als iemand oningelogd een beveiligde pagina bezoekt.
 
# Maak tabellen indien ze niet bestaan
@app.before_request
def create_tables():
    db.create_all()

# Zorgen dat het standaard pad zoals c:\blah in windows of /blah/ in linux opgehaald
# kan worden. Hierdoor kan er makkelijker naar bestanden worden gerefereerd.
basedir = os.path.abspath(os.path.dirname(__file__))

# Alle flask routes importeren uit routes.py
from routes import *
 
# Start de applicatie met extra feedback. Handig voor als de boel naar de klote gaat. (debug=true)
if __name__ == "__main__":
    app.run(debug=True)
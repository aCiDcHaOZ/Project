
#Nieuwe tabellen aanmaken, dit wordt gedaan door middel van Objecten in python ...

#Tabel gebruikers
class Gebruikers(db.Model):
    idnr = db.Column(db.Integer,primary_key=True)
    naam = db.Column(db.Text)
    email = db.Column(db.Text)
    telnr = db.Column(db.Text)

def __init__(self,naam,leeftijd):
    self.id = idnr
    self.naam = naam
    self.email = email
    self.telnr = telnr


#Bij error 404, laat 404.html zien
@app.errorhandler(404)
def pagina_niet_gevonden(e):
    return render_template("404.html"), 404

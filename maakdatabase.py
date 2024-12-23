import sqlite3
import os   #Om bestanden te detecteren en verwijderen, met name bungalow.db

# De optie bieden om een oude DB te verwijderen
if os.path.exists("bungalow.db"):
    if input("Oude bungalow bestand gevonden. Verwijderen? j/n ") == "j":
        os.remove("bungalow.db")

# Verbinding maken met SQLite-database (maakt een nieuwe als deze niet bestaat)
conn = sqlite3.connect('bungalow.db')
cursor = conn.cursor()

# Tabel maken: bungalows
cursor.execute('''
CREATE TABLE IF NOT EXISTS bungalows (
    bungalow_nummer INTEGER PRIMARY KEY,
    bungalow_naam TEXT NOT NULL
)
''')
cursor.executemany('''
INSERT INTO bungalows (bungalow_nummer, bungalow_naam)
VALUES (?, ?)
''', [
    (1, 'counterstrike'),
    (2, 'ageofempires'),
    (3, 'trackmania'),
])

# Tabel maken: boekingen
cursor.execute('''
CREATE TABLE IF NOT EXISTS Boekingen (
    boeking_id INTEGER PRIMARY KEY,
    bungalow_naam TEXT NOT NULL,
    klant_id REAL NOT NULL,
    boeking_prijs INTEGER NOT NULL,
    boeking_datumin DATE NOT NULL,
    boeking_datumuit DATE NOT NULL,
    FOREIGN KEY (bungalow_naam) REFERENCES bungalows(bungalow_id),
    FOREIGN KEY (klant_id) REFERENCES Gebruikers(klant_id)
)
''')

# Tabel maken: prijzen
cursor.execute('''
CREATE TABLE IF NOT EXISTS pakketten (
    pakketnummer INTEGER PRIMARY KEY,
    pakketnaam TEXT NOT NULL,
    pakketprijs TEXT NOT NULL
)
''')

#pakketprijzen tabel invullen
cursor.executemany(''' 
INSERT INTO pakketten (pakketnummer, pakketnaam, pakketprijs)
VALUES (?, ?, ?)
''', [
    (1, 'nachtpakket', '€129'),
    (2, 'weekendpakket', '€349'),
    (3, 'weekpakket', '€999'),
])



# Tabel maken: gebruikers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Gebruikers (
    klant_id INTEGER PRIMARY KEY,
    klant_naam TEXT NOT NULL,
    klant_telnr INTEGER NOT NULL,
    klant_email TEXT NOT NULL
)            
''')

# Tabel maken: lanparty
cursor.execute('''
CREATE TABLE IF NOT EXISTS lanparty (
    lan_id INTEGER PRIMARY KEY,
    lan_klantid INTEGER NOT NULL,
    lan_datum DATE NOT NULL,
    FOREIGN KEY (lan_klantid) REFERENCES Gebruikers(klant_id)
    
)            
''')
#een lanparty registreren
cursor.executemany(''' 
INSERT INTO lanparty (lan_id, lan_klantid, lan_datum)
VALUES (?, ?, ?)
''', [
    (1, 'campzone', '2025-01-01'),
    (2, 'thereality', '2025-02-01'),
])


conn.commit()

# Basisquery's uitvoeren
# 1. Alle artikelen opvragen
cursor.execute('SELECT * FROM bungalows')
bungalowsss = cursor.fetchall()
print("Bungalows:")
for bungalow in bungalowsss:
    print(bungalow)

# Verbinding sluiten
conn.close()

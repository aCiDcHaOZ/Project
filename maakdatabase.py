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
    bungalow_naam TEXT NOT NULL,
    bungalow_prijs REAL NOT NULL
)
''')
cursor.executemany('''
INSERT INTO bungalows (bungalow_nummer, bungalow_naam, bungalow_prijs)
VALUES (?, ?, ?)
''', [
    (1, 'Zonneschijn', 1200),
    (2, 'Sereen', 1000),
    (3, 'Exact', 800),
])

# Tabel maken: boekingen
cursor.execute('''
CREATE TABLE IF NOT EXISTS Boekingen (
    boeking_id INTEGER PRIMARY KEY,
    bungalow_naam TEXT NOT NULL,
    klant_id REAL NOT NULL,
    boeking_prijs INTEGER NOT NULL,
    FOREIGN KEY (bungalow_naam) REFERENCES bungalows(bungalow_id),
    FOREIGN KEY (klant_id) REFERENCES Gebruikers(klant_id)
)
''')

# Tabel maken: gebruikers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Gebruikers (
    klant_id INTEGER PRIMARY KEY,
    klant_naam TEXT NOT NULL
)            
''')



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

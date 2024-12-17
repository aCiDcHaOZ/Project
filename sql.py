import sqlite3


# Verbinding maken met SQLite-database (maakt een nieuwe als deze niet bestaat)
conn = sqlite3.connect('winkel.db')
cursor = conn.cursor()

# Tabellen maken
cursor.execute('''
CREATE TABLE IF NOT EXISTS artikel (
    artikel_id INTEGER PRIMARY KEY,
    naam TEXT NOT NULL,
    prijs REAL NOT NULL
)
''')

# Data invoegen
cursor.executemany('''
INSERT INTO artikel (naam, prijs)
VALUES (?, ?)
''', [
    ('Laptop', 1200.50),
    ('Muismat', 10.99),
    ('Toetsenbord', 45.75),
])

conn.commit()

# Basisquery's uitvoeren
# 1. Alle artikelen opvragen
cursor.execute('SELECT * FROM artikel')
artikelen = cursor.fetchall()
print("Artikelen:")
for artikel in artikelen:
    print(artikel)

# Verbinding sluiten
conn.close()

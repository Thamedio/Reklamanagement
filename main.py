import sqlite3
import os
from dao import create_tables

# Verzeichnis und Datenbankname
db_directory = r"\\MS01\Datenpfad\ReklaDB"
db_filename = "reklamationen.db"
db_path = os.path.join(db_directory, db_filename)

# Verbindung zur Datenbank herstellen (wenn die Datenbank nicht existiert, wird sie erstellt)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabellen erstellen
create_tables(cursor)

# Verbindung schließen
conn.commit()
conn.close()

print(f"Datenbank '{db_filename}' wurde erfolgreich im Verzeichnis '{db_directory}' erstellt und Tabellen wurden angelegt.")
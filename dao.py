from sqlitedao import SqliteDao
from sqlitedao import ColumnDict

create_table_columns_reklaData = {
    "reklamationsID": "TEXT",
    "deadline": "DATE",
    "verantwortlich": "TEXT",
    "reklaTyp": "TEXT",
    "artikelNrMothes": "TEXT",
    "teileNrKunde": "TEXT",
    "zeichnungsNr": "TEXT",
    "revision": "TEXT",
    "bezeichnung": "TEXT",
    "kunde": "TEXT",
    "initDate": "DATE",
    "stueckzahlGesamt": "INTEGER",
    "stueckzahlNio": "INTEGER",
    "projektNr": "INTEGER",
    "lieferscheinNr": "TEXT",
    "bestellNr": "TEXT",
    "zuordnung": "TEXT",
    "status": "TEXT",
    "standort": "TEXT",
    "kosten": "FLOAT"
}

create_table_columns_8D = {
    "reklamationsID": "TEXT",
    "8D_D0": "TEXT",
    "8D_D1": "TEXT",
    "8D_D1_verantwortlich": "TEXT",
    "8D_D1_dueDate": "DATE",
    "8D_D1_doneDate": "DATE",
    "8D_D2": "TEXT",
    "8D_D2_verantwortlich": "TEXT",
    "8D_D2_dueDate": "DATE",
    "8D_D2_doneDate": "DATE",
    "8D_D3": "TEXT",
    "8D_D3_verantwortlich": "TEXT",
    "8D_D3_dueDate": "DATE",
    "8D_D3_doneDate": "DATE",
    "8D_D4": "TEXT",
    "8D_D4_verantwortlich": "TEXT",
    "8D_D4_dueDate": "DATE",
    "8D_D4_doneDate": "DATE",
    "8D_D5": "TEXT",
    "8D_D5_verantwortlich": "TEXT",
    "8D_D5_dueDate": "DATE",
    "8D_D5_doneDate": "DATE",
    "8D_D6": "TEXT",
    "8D_D6_verantwortlich": "TEXT",
    "8D_D6_dueDate": "DATE",
    "8D_D6_doneDate": "DATE",
    "8D_D7": "TEXT",
    "8D_D7_verantwortlich": "TEXT",
    "8D_D7_dueDate": "DATE",
    "8D_D7_doneDate": "DATE",
    "8D_D8": "TEXT",
    "8D_D8_verantwortlich": "TEXT",
    "8D_D8_dueDate": "DATE",
    "8D_D8_doneDate": "DATE"
}

create_table_columns_RAG = {
    "reklamationsID": "TEXT",
    "RAG": "INTEGER",
    "RAG_anweisung": "TEXT",
    "RAG_bemerkung": "TEXT",
    "sz_agBeginn": "INTEGER",
    "sz_agEnde_iO": "INTEGER",
    "sz_agEnde_niO": "INTEGER",
    "pNr_werker": "INTEGER",
    "maschine": "TEXT",
    "ts_beginn": "DATE",
    "ts_ende": "DATE",
    "dauer": "integer"

}

def create_tables(cursor):
    # Erstellung der Tabelle reklaData
    reklaData_columns = ", ".join([f'"{col}" {datatype}' for col, datatype in create_table_columns_reklaData.items()])
    create_reklaData_table = f"CREATE TABLE IF NOT EXISTS reklaData ({reklaData_columns})"
    cursor.execute(create_reklaData_table)

    # Erstellung der Tabelle reports
    reports_columns = ", ".join([f'"{col}" {datatype}' for col, datatype in create_table_columns_8D.items()])
    create_reports_table = f"CREATE TABLE IF NOT EXISTS reports ({reports_columns})"
    cursor.execute(create_reports_table)

    # Erstellung der Tabelle RAGs
    RAGs_columns = ", ".join([f'"{col}" {datatype}' for col, datatype in create_table_columns_RAG.items()])
    create_RAGs_table = f"CREATE TABLE IF NOT EXISTS RAGs ({RAGs_columns})"
    cursor.execute(create_RAGs_table)

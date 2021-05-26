import sqlite3
from sqlite3.dbapi2 import connect
from DATACLASS import nomFichier
import logging
import json
import tempfile


def sql_db_creation():
    try:
        conn = sqlite3.connect("pass_data.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS PassDataBase
            (
                Site TEXT, 
                Login TEXT, 
                Pass TEXT
            )
        """)
        conn.close()
    except sqlite3.Error as er:
        logging.error(f"Erreur lors dela connexion à la base : {er}")
    else:
        logging.info("Connexion à la base reussie")


def save_to_sql():
    try:
        #Sauvegarde dans la db
        conn = sqlite3.connect("pass_data.db")
        c = conn.cursor()
        with tempfile.TemporaryFile() as f:
            testDict = f.read()
        with open(nomFichier, "r") as f:
            dataDict = json.load(f)
        print(dataDict)
        c.executemany("""INSERT INTO pass_data VALUES (?,?)""",dataDict)
        conn.commit()
        conn.close()

        #Suppression du fichier json

    except json.JSONDecodeError as er:
        logging.error(f"Erreur de décodage json : {er.msg}")
    except sqlite3.Error as er:
        logging.error(f"Sauvegarde Echouée : {er}")
    else:
        logging.info("Données sauvegarder avec Success")


def get_from_sql():
    try:
        conn = sqlite3.connect("pass_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM pass_data")
        newDatadict = c.fetchall()
        conn.close()
        with open(nomFichier, "w") as f:
            json.dump(newDatadict, f, indent=4)
        

    except sqlite3.Error as er:
        logging.error(f"Erreur lors de la recuperation des données: {er}")
    else:
        logging.info("Données recuperées avec success")
    
    return newDatadict


    






if __name__ == "__main__":
    save_to_sql()
    get_from_sql()

from hashlib import new
from DATACLASS import DATA
import sqlite3
import json
import tempfile
import logging
import os


tempdir = function


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


def save_to_sql():  # sourcery skip
    try:
        dataDict = DATA.get_data()
        conn = sqlite3.connect("pass_data.db")
        c = conn.cursor()
        c.executemany("""INSERT INTO pass_data VALUES (?,?)""",dataDict)
        conn.commit()
        conn.close()
    except json.JSONDecodeError as er:
        logging.error(f"Erreur de décodage json : {er.msg}")
    except sqlite3.Error as er:
        logging.error(f"Sauvegarde Echouée : {er}")
    else:
        logging.info("Données sauvegarder avec Success")


def get_from_sql():  # sourcery skip
    try:
        conn = sqlite3.connect("pass_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM pass_data")
        newDatadict = c.fetchall()
        conn.close()
        return newDatadict
    except sqlite3.Error as er:
        logging.error(f"Erreur lors de la recuperation des données: {er}")

    except os.error as er:
        logging.error(f"Erreur Système : {er}")
    else:
        logging.info("Données recuperées avec success")


if __name__ == "__main__":
    save_to_sql()
    test = get_from_sql()
    DATA.save_data(test)

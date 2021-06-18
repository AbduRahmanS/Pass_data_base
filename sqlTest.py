from DATACLASS import DATA
import sqlite3, json, tempfile, logging, os
from _vars import loadJson, dumpJson


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


def save_to_sql():
    try:
        if os.path.exists(jsonFilePath):
            with open(jsonFilePath, "r") as f:
                dataDict = json.load(f)
            return dataDict
        else:
            logging.error(f"Fichier temporaire introuvable")

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


def get_from_sql():
    tempdir = tempfile.mkdtemp()
    global jsonFilePath
    jsonFilePath = os.path.join(tempdir, 'data.json')
    try:
        conn = sqlite3.connect("pass_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM pass_data")
        newDatadict = c.fetchall()
        conn.close()
        with open (jsonFilePath, "w") as f:
            json.dump(newDatadict,f, indent=4)
    
    except sqlite3.Error as er:
        logging.error(f"Erreur lors de la recuperation des données: {er}")
    
    except os.error as er:
        logging.error(f"Erreur Système : {er}")
    else:
        logging.info("Données recuperées avec success")


    






if __name__ == "__main__":
    save_to_sql()
    get_from_sql()

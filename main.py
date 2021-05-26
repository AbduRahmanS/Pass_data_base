"""
------ PasswordDataBase -----
Programme permettant la gestion de mot de passe dans une base de données.
Lorsque vous executer le programme, les données sont temporairement sauvegarder
dans un fichier json; et seront ensuite tranferer dans une bd sqlite3 à la fin du programme.

Note : 
-   l'interface graphique du programme n'est pas operationnel,
-   Ce code est pour but éducatif, vos suggetions et amélioration sont les bienvenue

"""

import logging
from DATACLASS import DATA


action = DATA("","","")
continuer = 0
while continuer != 5:
    print(" Password DataBase ".center(50,"*"))
    print(" >> 1. Ajouter\n >> 2. Supprimer\n >> 3. Modifier \n >> 4. Tout Afficher\n >> 5. Rechercher\n >> 6. Quittez")
    try:
        continuer = int(input("\n >>>>> "))
    except ValueError:
        print("Valeur incorrecte, Reessayer")

    
    
    if continuer == 1:
        nomSite = input(">> Site : ")
        login = input(">> Login : ")
        motDePass = input(">> Password : ")
        action = DATA(nomSite, login,motDePass)
        action.add_data()
    elif continuer == 2:
        siteAsupprimer = str(input("Nom du site a Supprimer : "))
        action.remove_data(siteAsupprimer)
    elif continuer == 3:
        siteAmodifier = input("Site a modifier : ")
        newLogin = input("Nouveau Login : ")
        newPass = input("Nouveau Pass : ")
        action.set_data(siteAmodifier, newLogin, newPass)
    elif continuer == 4:
        allData = action.get_data()
        i = 1
        for cle,valeur in allData.items():
            log = valeur["Login"]
            mpass = valeur["Password"]
            print(f"{i}|{cle} : Login --> {log} | Pass --> {mpass}")
            i += 1
    elif continuer == 5:
        dataToFind = input("Site a rechercher : ")
        datas = action.get_data()
        for cle in datas.keys():
            if dataToFind == cle:
                print(f"Site Trouver: {cle} --> {datas[cle]}")
            else:
                logging.warning("Ce site n'est pas dans la base")
    elif continuer == 6:
        break
    else:
        print("Erreur Choix indisponible")
        continue
        


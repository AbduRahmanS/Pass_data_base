from ast import With
import json
import logging
import os
import tempfile

logging.basicConfig(filename='journal.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s --> %(message)s')
logging.debug('Exécution du programme reussie !')


class DATA:
    tempdir = tempfile.mkdtemp(suffix="pass_data")
    jsonFilePath = os.path.join(tempdir + '/Data.json')

    @classmethod
    def get_data(cls) -> dict:
        if os.path.exists(cls.jsonFilePath):
            with open(cls.jsonFilePath, "r") as f:
                data_dict = json.load(f)        
            return data_dict
        else:
            data_dict = {}
            with open(cls.jsonFilePath,"w") as f:
                json.dump(data_dict, f)

    @classmethod
    def save_data(cls, datas):
        with open(cls.jsonFilePath, 'w') as f:
            json.dump(datas, f, indent=4)
            
    @classmethod
    def del_tempdir(cls):
        with open(cls.tempdir, 'r') as f:
            pass


    @staticmethod
    def add_data(site_name, login, password)    :  # sourcery skip: dict-literal
        datas = DATA.get_data()
        if site_name not in datas:
            datas[site_name] = {'Login': login, 'Password': password}
            DATA.save_data(datas)
            logging.info("Enregistrement Effectuée")
            return True
        else:
            logging.warning(f'le site {site_name} existe déja')
            return False
        
    @staticmethod
    def remove_data(nom_site):
        datas = DATA.get_data()
        if nom_site in datas:
            del datas[nom_site]
            DATA.save_data(datas)
            logging.info('Suppression Effectuée')
            return True
        else:
            logging.warning(f'Erreur Supression, le site {nom_site} est introuvable')
            return False

    @staticmethod
    def set_data(site_name, new_login, new_pass):
        # sourcery skip: dict-literal, remove-dict-keys
        datas = DATA.get_data()
        if site_name in datas.keys():
            datas[site_name] = {"Login": new_login, "Password": new_pass}
            logging.info("Modification Effectuée")
            DATA.save_data(datas)
            return True
        else:
            logging.warning(f"le site {site_name} n'est pas dans la base")
            return False


if __name__ == '__main__':
    DATA.add_data("test_site","testlogin","testpassword")
    DATA.add_data("site1","login1","password1")
    DATA.set_data("site1", "login2", "password2")
    DATA.remove_data("test_site")
    
    print(DATA.get_data())
    

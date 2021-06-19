import json
import logging
import os
import tempfile

logging.basicConfig(filename='journal.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s --> %(message)s')
logging.debug('Exécution du programme reussie !')


class DATA:
    tempdir = tempfile.mkdtemp()
    jsonFilePath = os.path.join(tempdir + '/Data.json')

    # def __str__(self):
    #     _dict = {self.siteName: {'Login': self.login, 'Password': self.password}}
    #     return _dict

    @classmethod
    def get_data(cls):
        if os.path.exists(cls.jsonFilePath):
            with open(cls.jsonFilePath, "r") as f:
                data_dict = json.load(f)
            return data_dict

    @classmethod
    def save_data(cls, datas):
        with open(cls.jsonFilePath, 'w') as f:
            json.dump(datas, f, indent=4)

    @staticmethod
    def add_data(site_name, login, password):  # sourcery skip: dict-literal
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
    print(DATA.jsonFilePath)

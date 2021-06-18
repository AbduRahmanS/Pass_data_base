
import os, json, logging, tempfile
from _vars import loadJson, dumpJson


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
                dataDict = json.load(f)
    @classmethod
    def save_data(cls, datas):
        with open(cls.jsonFilePath, 'w') as f:
            json.dump(datas, f, indent=4)

    @staticmethod
    def add_data(siteName, login, password):
        datas = DATA.get_data()
        datas = dict()
        if siteName not in datas:
            datas[siteName] = {'Login': login, 'Password': password}
            DATA.save_data(datas)
            logging.info("Enregistrement Effectuée")
            return True
        else:
            logging.warning(f'le site {siteName} existe déja')
            return False

    @staticmethod
    def remove_data(nomSite):
        datas = DATA.get_data()
        if nomSite in datas:
            del datas[nomSite]
            DATA.save_data(datas)
            logging.info('Suppression Effectuée')
            return True
        else:
            logging.warning(f'Erreur Supression, le site {nomSite} est introuvable')
            return False
            
    @staticmethod
    def set_data(siteName, newLogin, newPass):
        datas = DATA.get_data()
        datas = dict()
        if siteName in datas.keys():
            datas[siteName] = {"Login":newLogin, "Password":newPass}
            logging.info("Modification Effectuée")
            DATA.save_data(datas) 
            return True
        else:
            logging.warning(f"le site {siteName} n'est pas dans la base")
            return False


    
if __name__ == '__main__':
    print(DATA.jsonFilePath)

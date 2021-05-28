import json, logging
from _vars import loadJson, dumpJson


logging.basicConfig(filename='journal.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s --> %(message)s')
logging.debug('Exécution du programme reussie !')


class DATA:
    def __init__(self, siteName, login, password):
        self.siteName = siteName
        self.login = login
        self.password = password
    
    def __str__(self):
        _dict = {self.siteName: {'Login': self.login, 'Password': self.password}}
        return _dict
    
    def get_data(self):
        return loadJson()
    
    def save_data(self, datas):
        dumpJson(datas)


    def add_data(self):
        datas = self.get_data()
        if self.siteName not in datas:
            datas[self.siteName] = {'Login': self.login, 'Password': self.password}
            self.save_data(datas)
            logging.info("Enregistrement Effectuée")
            return True
        else:
            logging.warning(f'le site {self.siteName} existe déja')
            return False

    def remove_data(self, nomSite):
        datas = self.get_data()
        if nomSite in datas:
            del datas[nomSite]
            self.save_data(datas)
            logging.info('Suppression Effectuée')
            return True
        else:
            logging.warning(f'Erreur Supression, le site {self.siteName} est introuvable')
            return False
    
    def set_data(self, siteName, newLogin, newPass):
        datas = self.get_data()
        if siteName in datas.keys():
            datas[siteName] = {"Login":newLogin, "Password":newPass}
            logging.info("Modification Effectuée")
            self.save_data(datas) 
            return True
        else:
            logging.warning(f"le site {self.siteName} n'est pas dans la base")
            return False


    



if __name__ == "__main__":
    
    test = DATA("testSiteTest","login","password")
    test.add_data()
    test.remove_data("testsite")
    test.remove_data("testsite2")
    test.set_data("testsite", "newlogin", "newpassword")
    
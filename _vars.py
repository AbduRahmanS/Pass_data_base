import os, tempfile, json


tempdir = tempfile.mkdtemp()
jsonFilePath = os.path.join(tempdir + '/Data.json')


def loadJson():
    if os.path.exists(jsonFilePath):
        with open(jsonFilePath, "r") as f:
            dataDict = json.load(f)
        
        return dataDict


def dumpJson(dataTodump):
    with open(jsonFilePath, 'w') as f:
            json.dump(dataTodump, f, indent=4)


import json

class File:
    def __init__(self, fileName):
        self.fileName=fileName
        self.dataJSON = {}
        self.newPolylines = []

    def read(self):
        try:
            with open(self.fileName, "r", encoding="UTF-8") as loadFile:
                self.dataJSON = json.load(loadFile)
                return self.dataJSON["features"]
        except PermissionError:
            print(f"Nemáš umožněný přístup do souboru {self.fileName}")
            exit()
        except ValueError:
            print(f"V souboru {self.fileName} je chyba")
            exit()
        except FileNotFoundError:
            print(f"Soubor {self.fileName} nebyl nalezen")
            exit()

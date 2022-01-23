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

    def write(self):
        try:
            with open(self.fileName, "w", encoding="UTF-8") as writefile:
                parties = []
                for polyline in self.newPolylines:
                    parties.append(polyline.get_object_for_json())
                self.dataJSON["features"] = parties
                json.dump(self.dataJSON, writefile)
        except PermissionError:
            print(f"CHYBA: Nemam pristup k {self.fileName}. Program skonci.")
            exit()
        except:
            print(f"CHYBA: Nemuzu ulozit soubor.")
            exit()
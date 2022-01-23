import json

class File:
    def __init__(self, name):
        self.name=name
        self.polylines = []
        self.json_data = {}

    def read(self):
        try:
            with open(self.name, "r", encoding="UTF-8") as physicFile:
                self.json_data = json.load(physicFile)
                return self.json_data["features"]
        except FileNotFoundError: # zjistuje, zda existuje
            print(f"CHYBA: Pozadovany soubor {self.name} neexistuje. Program skonci.")
            exit()
        except PermissionError: # zjistuje pristup k souboru
            print(f"CHYBA: Nemam pristup k {self.name}.Program skonci.")
            exit()
        except ValueError as e: # validuje i pokud se jedna o validni JSON
            print(f"CHYBA: Soubor {self.name} neni validni. Program skonci.\n", e)
            exit()

    def write(self):
        try:
            with open(self.name, "w", encoding="UTF-8") as physicFile:
                features = []
                for polyline in self.polylines:
                    features.append(polyline.get_object_for_json())
                self.json_data["features"] = features
                json.dump(self.json_data, physicFile)
        except PermissionError: # zjistuje pristup k souboru
            print(f"CHYBA: Nemam pristup k {self.name}. Program skonci.")
            exit()
        except:
            print(f"CHYBA: Nemuzu ulozit soubor.")
            exit()
import json

#TŘÍDA UMOŽŇUJÍCÍ ČTENÍ SOUBORU A JEHO ZÁPIS
class GeoJSON:
    def __init__(self, fileName):
        self.fileName=fileName
        self.polylines = []
        self.geoJSONData = {}

    #NAHRÁNÍ SOUBORU S VÝJIMKAMI
    def read(self):
        try:
            with open(self.fileName, "r", encoding="UTF-8") as loadedFile:
                self.geoJSONData = json.load(loadedFile)
                return self.geoJSONData["features"] #získání dat, ve kterých jsou sořadnice
        except ValueError as e:
            print(f"Nahráný soubor obsahuje chybu na řádku", e)
            exit()
        except FileNotFoundError: 
            print(f"Soubor {self.fileName} se nepodařilo nalézt")
            exit()
        except PermissionError:
            print(f"Nemáš povolený přístup k datům.")
            exit()

    #ZÁPIS NOVÝCH DAT DO NOVÉHO SOUBORU
    def write(self):
        try:
            with open(self.fileName, "w", encoding="UTF-8") as loadedFile:
                newPolylines = [] #definice prázdné množiny, ve které budou nové souřadnice
                for polyline in self.polylines: #postupné zapisování polylines do dílčí proměnné
                    newPolylines.append(polyline.attributteNewJSON())
                self.geoJSONData["features"] = newPolylines
                json.dump(self.geoJSONData, loadedFile) #samotné vytvoření souboru
        except PermissionError: 
            print(f"Nemáš povolený zápis do souboru")
            exit()
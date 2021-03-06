import argparse
from LoadGEOJSON import GeoJSON
from Polyline import Polyline

#ZPROCESOVÁNÍ CELÉHO PŘÍKLADU
def process(max_length, fileName):
    allPolylines = [] #všechny segmenty, polylines
    for data in fileName:
        try:
            if data["geometry"]["type"] == "LineString": #následující části kódu se probedou, pokud se jedná o datový typ linestring
                polylineNew = Polyline(data)
                allPolylines.append(polylineNew.divide_long_segments(max_length))
            elif data["geometry"]["type"] != "LineString":
                print("Chybná data:", data["properties"]["OBJECTID"])
        except KeyError: 
            print("Chybí data")
            exit()
    return allPolylines

#DEFINOVÁNÍ PARAMETRŮ PRO VOLÁNÍ PROGRAMU
parser = argparse.ArgumentParser(description="Zadej povinné parametry")
parser.add_argument('-f', '--file', default=None, required=True, help="Zadej název vstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-o', '--output', default=None, required=True, help="Zadej název výstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-l', '--length', default=None, required=True, type=float, help="Zadej maximální vzdálenost segmentu")
args = parser.parse_args()

namedFile = GeoJSON(args.file) #načtení nového souboru (čtení)
data = namedFile.read() #přečtení souboru
namedFileW = namedFile #rozdílné pojmenování souboru
namedFileW.polylines = process(args.length, data) #samotný proces
namedFileW.fileName = args.output #definovní zápisu
namedFileW.write() #zápis do nového souboru
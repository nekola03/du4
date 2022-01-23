import argparse
from LoadGEOJSON import loadGeoJSON
from Polyline import polyline

#ZPROCESOVÁNÍ CELÉHO PŘÍKLADU
def process(max_length, fileName):
    allPolylines = [] #všechny segmenty, polylines
    for data in fileName:
        try:
            if data["geometry"]["type"] == "LineString": #následující části kódu se probedou, pokud se jedná o datový typ linestring
                polylineNew = polyline(data)
                allPolylines.append(polylineNew.divide_long_segments(max_length))
            elif data["geometry"]["type"] != "LineString":
                print("Chybná data:", data["properties"]["OBJECTID"])
        except: 
            print("Chybí data")
            exit()
    return allPolylines

#DEFINOVÁNÍ PARAMETRŮ PRO VOLÁNÍ PROGRAMU
parser = argparse.ArgumentParser(description="Zadej povinné parametry")
parser.add_argument('-f', '--file', default=None, help="Zadej název vstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-o', '--output', default=None, help="Zadej název výstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-l', '--length', default=None, help="Zadej maximální vzdálenost segmentu")
args = parser.parse_args()
if args.file is not None and args.length is not None and args.output is not None: #provede se v případě, že byly určeny argumenty
    namedFile = loadGeoJSON(args.file) #načtení nového souboru
    data = namedFile.read() #přečtení souboru
    namedFile.polylines = process(float(args.length), data) #samotný proces
    namedFile.fileName = args.output #definovní zápisu
    namedFile.write() #zápis do nového souboru
else:
    print("Chybně zadané parametry")
    exit()
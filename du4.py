import argparse
from LoadGEOJSON import loadGeoJSON
from Polyline import polyline

def process(max_length, fileName):
    allPolylines = []
    for data in fileName:
        try:
            if data["geometry"]["type"] == "LineString":
                polylineNew = polyline(data)
                allPolylines.append(polylineNew.divide_long_segments(max_length))
            elif data["geometry"]["type"] != "LineString":
                print("Chybná data:", data["properties"]["OBJECTID"])
        except:
            print("Chybí data")
            exit()
    return allPolylines

parser = argparse.ArgumentParser(description="Zadej povinné parametry")
parser.add_argument('-f', '--file', default=None, help="Zadej název vstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-o', '--output', default=None, help="Zadej název výstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-l', '--length', default=None, help="Zadej maximální vzdálenost segmentu")
args = parser.parse_args()
if args.file is not None and args.length is not None and args.output is not None:
    namedFile = loadGeoJSON(args.file)
    data = namedFile.read()
    namedFile.polylines = process(float(args.length), data)
    namedFile.fileName = args.output
    namedFile.write()
else:
    print("Chybně zadané parametry")
    exit()
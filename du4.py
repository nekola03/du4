import argparse
from LoadGEOJSON import File
from Polyline import Polyline

def process(file, max_length):
    multilines = []
    for readsData in file:
        try:
            if readsData["geometry"]["type"] == "LineString":
                polyline = Polyline(readsData)
                multilines.append(polyline.divide_long_segments(max_length))
            elif readsData["geometry"]["type"] != "LineString":
                print("Chybná data:", readsData["properties"]["OBJECTID"])
        except KeyError:
            print("Chybí data")
            exit()
    return multilines

parser = argparse.ArgumentParser(description="Zadej povinné parametry")
parser.add_argument('-f', '--file', default=None, help="Zadej název vstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-o', '--output', default=None, help="Zadej název výstupního souboru s příponou GEOJSON či JSON")
parser.add_argument('-l', '--length', default=None, help="Zadej maximální vzdálenost segmentu")
args = parser.parse_args()
if args.file != None and args.length != None and args.output != None:
    file = File(args.file)
    data = file.read()
    file.polylines = process(data, float(args.length))
    file.name = args.output
    file.write()
else:
    print("Chybně zadané parametry")
    exit()
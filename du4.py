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
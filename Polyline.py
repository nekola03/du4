from Point import Point
import Segment

#TŘÍDA PRO KONSTRUKCI POLYLINE
class Polyline:
    def __init__(self, data=None):
        self.lines = []
        self.data = data
        if data is not None: #pokud existují data provedou se následující metody
            self.process()

    #ZPROCESOVÁNÍ DAT
    def process(self):
        lineTMP = Segment.Segment()
        for pointFromData in self.data["geometry"]["coordinates"]: #cyklus procházení konkrétních atribudů a jejich výběr
            pointSpecific = Point(pointFromData[0], pointFromData[1])
            if lineTMP.pointFirst is not None: #vytvoření, resp. zprocesování segmentu na základě podmínky
                lineTMP.pointSecond = pointSpecific
                self.segmentAdd(lineTMP)
                lineTMP = Segment.Segment(pointSpecific) #tvorba segmentů v jednotlivé polyline
            elif lineTMP.pointFirst is None: 
                lineTMP.pointFirst = pointSpecific

    #PŘÍPRAVA NOVÝCH DAT PRO ZÁPIS
    def attributteNewJSON(self):
        coords = []
        rightPos = 1
        for segment in self.lines: #zápis do do atrbutu na základě podmínky pozice
            if not rightPos:
                coords.append([segment.pointFirst.x, segment.pointFirst.y])
                rightPos = 0
            coords.append([segment.pointSecond.x, segment.pointSecond.y])
        self.data["geometry"]["coordinates"] = coords #vložení nových atributů do kódu
        return self.data

    #PŘIDÁNÍ POLYLINE A SEGMENTU A ROZDĚLENÍ DELŠÍHO SEGMENTU
    def polylineAdd(self, moreSegment):  #přidání segmentu na základě následující funkce
        for segment in moreSegment.lines:
            self.segmentAdd(segment)
    
    def segmentAdd(self, segment): #přídání segmentu do lines
        self.lines.append(segment)

    def divide_long_segments(self, max_length): #rozdělení douhého segmentu
        polylineNew = Polyline()
        polylineNew.data = self.data
        for line in self.lines: #postupné procházení segmentů a jejich výstup v nových polylines
            polylineTMP = line.divide(max_length) #dělení na základě metody v třídě segment
            polylineNew.polylineAdd(polylineTMP)
        return polylineNew
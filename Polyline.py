from Point import Point
import Segment

class Polyline:
    def __init__(self, data=None):
        self.lines = []
        self.data = data
        if data is not None:
            self.process()

    def process(self):
        lineTMP = Segment.Line()
        for pointFromData in self.data["geometry"]["coordinates"]:
            pointSpecific = Point(pointFromData[0], pointFromData[1])
            if lineTMP.pointFirst is not None:
                lineTMP.pointSecond = pointSpecific
                self.segmentAdd(lineTMP)
                lineTMP = Segment.Line(pointSpecific)
            elif lineTMP.pointFirst is None: 
                lineTMP.pointFirst = pointSpecific

    def polylineAdd(self, polyline):
        for line in polyline.lines:
            self.segmentAdd(line)
    
    def segmentAdd(self, segment):
        self.lines.append(segment)

    def divide_long_segments(self, max_length):
        polylineNew = Polyline()
        polylineNew.data = self.data

        for line in self.lines:
            polylineTMP = line.divide(max_length)
            polylineNew.polylineAdd(polylineTMP)

        return polylineNew

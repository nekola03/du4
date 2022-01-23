from math import sqrt
import Polyline
from Point import Point

class Line:
    def __init__(self, pointFirst=None, pointSecond=None):
        self.pointFirst = pointFirst
        self.pointSecond = pointSecond
        self.PointBetween = None
        self.length = None

    def calculateOneCoor(self, coorFirst, coorSecond):
        oneCoor = (coorFirst+coorSecond)/2
        return oneCoor

    def calculatePointBetween(self):
        xAxisMid = self.calculateOneCoor(self.pointFirst.x, self.pointSecond.x)
        yAxisMid = self.calculateOneCoor(self.pointFirst.y, self.pointSecond.y)
        self.PointBetween = Point(xAxisMid, yAxisMid)

    def distance(self):
        self.length = sqrt((self.pointFirst.x - self.pointSecond.x)**2 + (self.pointFirst.y - self.pointSecond.y)**2)
        return self.length

    def divide(self, max_length):
        createPol = Polyline.Polyline()

        if self.distance()>=max_length:
            self.calculatePointBetween()
            createPol.segmentAdd(Line(self.pointFirst, self.PointBetween)) #importováno z Polyline
            createPol.segmentAdd(Line(self.PointBetween, self.pointSecond)) #importováno z Polyline
            return createPol.divide_long_segments(max_length) #importováno z Polyline

        createPol.segmentAdd(self) #importováno z Polyline
        return createPol
from Point import point
import Polyline
from math import sqrt

class segment:
    def __init__(self, pointFirst=None, pointSecond=None):
        self.pointFirst = pointFirst
        self.pointSecond = pointSecond
        self.PointBetween = 0
        self.length = 0

    def calculateOneCoor(self, coorFirst, coorSecond):
        oneCoor = (coorFirst+coorSecond)/2
        return oneCoor

    def calculatePointBetween(self):
        self.PointBetween = point(self.calculateOneCoor(self.pointFirst.x, self.pointSecond.x), self.calculateOneCoor(self.pointFirst.y, self.pointSecond.y))

    def distance(self):
        self.length = sqrt((self.pointFirst.x - self.pointSecond.x)**2 + (self.pointFirst.y - self.pointSecond.y)**2)
        return self.length

    def divide(self, max_length):
        createPolyline = Polyline.polyline()
        if self.distance() >= max_length:
            self.calculatePointBetween()
            createPolyline.segmentAdd(segment(self.pointFirst, self.PointBetween)) 
            createPolyline.segmentAdd(segment(self.PointBetween, self.pointSecond)) 
            return createPolyline.divide_long_segments(max_length) 

        createPolyline.segmentAdd(self) 
        return createPolyline
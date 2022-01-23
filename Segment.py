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
        middle_x = self.calculateOneCoor(self.pointFirst.x, self.pointSecond.x)
        middle_y = self.calculateOneCoor(self.pointFirst.y, self.pointSecond.y)
        self.PointBetween = Point(middle_x, middle_y)

    def distance(self):
        self.length = sqrt((self.pointFirst.x - self.pointSecond.x)**2 + (self.pointFirst.y - self.pointSecond.y)**2)
        return self.length
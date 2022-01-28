from Point import Point
import Polyline
from math import sqrt

#VYTVOŘENÍ TŘÍDY
class Segment:
    def __init__(self, pointFirst=None, pointSecond=None):
        self.pointFirst = pointFirst
        self.pointSecond = pointSecond
    
    #VÝPOČET SEGMENTU NA ZÁKLADĚ SOUŘADNIC 2 BODŮ
    def calculateOneCoor(self, coorFirst, coorSecond): #výpočet souřadnice na jedné z os
        oneCoor = (coorFirst+coorSecond)/2
        return oneCoor
    
    def calculatePointBetween(self): #výpočet souřadnice na jedné ose s přiřazením souřadnice
        self.PointBetween = Point(self.calculateOneCoor(self.pointFirst.x, self.pointSecond.x), self.calculateOneCoor(self.pointFirst.y, self.pointSecond.y))

    def distance(self): #výpočet vzdálenosti segmentu pythagorovou větou
        self.length = sqrt((self.pointFirst.x - self.pointSecond.x)**2 + (self.pointFirst.y - self.pointSecond.y)**2)
        return self.length

    #ROZDĚLENÍ SOUŘASNÉHO SEGMENTU
    def divide(self, max_length):
        createPolyline = Polyline.Polyline() #třída v proměnné
        if self.distance() >= max_length: #vytvoření třídy pokud je segment menší než maximální vzdálenost
            self.calculatePointBetween()
            createPolyline.segmentAdd(Segment(self.pointFirst, self.PointBetween)) 
            createPolyline.segmentAdd(Segment(self.PointBetween, self.pointSecond)) 
            return createPolyline.divide_long_segments(max_length) #navrácení vytvořeného segmentu
        createPolyline.segmentAdd(self) 
        return createPolyline #vytvoření polyline ze všech segmentů
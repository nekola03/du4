from Point import point
import Polyline
from math import sqrt

#VYTVOŘENÍ TŘÍDY
class segment:
    def __init__(self, pointFirst=None, pointSecond=None):
        self.pointFirst = pointFirst
        self.pointSecond = pointSecond
        self.PointBetween = 0
        self.length = 0
    
    #VÝPOČET SEGMENTU NA ZÁKLADĚ SOUŘADNIC 2 BODŮ
    def calculateOneCoor(self, coorFirst, coorSecond): #výpočet souřadnice na jedné z os
        oneCoor = (coorFirst+coorSecond)/2
        return oneCoor
    
    def calculatePointBetween(self): #výpočet souřadnice na jedné ose s přiřazením souřadnice
        self.PointBetween = point(self.calculateOneCoor(self.pointFirst.x, self.pointSecond.x), self.calculateOneCoor(self.pointFirst.y, self.pointSecond.y))

    def distance(self): #výpočet vzdálenosti segmentu pythagorovou větou
        self.length = sqrt((self.pointFirst.x - self.pointSecond.x)**2 + (self.pointFirst.y - self.pointSecond.y)**2)
        return self.length

    #ROZDĚLENÍ SOUŘASNÉHO SEGMENTU
    def divide(self, max_length):
        createPolyline = Polyline.polyline() #třída v proměnné
        if self.distance() >= max_length: #vytvoření třídy pokud je segment menší než maximální vzdálenost
            self.calculatePointBetween()
            createPolyline.segmentAdd(segment(self.pointFirst, self.PointBetween)) 
            createPolyline.segmentAdd(segment(self.PointBetween, self.pointSecond)) 
            return createPolyline.divide_long_segments(max_length) #navrácení vytvořeného segmentu
        createPolyline.segmentAdd(self) 
        return createPolyline #vytvoření polyline ze všech segmentů
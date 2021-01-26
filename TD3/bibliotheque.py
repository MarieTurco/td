from collections import namedtuple
from math import * 

def fonction2():
  return 2


Point1D = namedtuple("Point1D", ["x"])

Point2D = namedtuple("Point2D", "x y")



def ajout_point1d(point1, point2):
  x = point1.x + point2.x
  return Point1D(x)


def norme1d(p1):
    return (p1.x ** 2) ** 0.5 

def moyenne(liste):
    return (sum(liste)/len(liste))

def variance(liste):
    moy_=moyenne(liste)
    d2 = [(x-moy_)**2 for x in liste]
    return moyenne(d2)

def ecart_type(liste):
    return sqrt(variance(liste))


assert True
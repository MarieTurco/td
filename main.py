from collections import namedtuple

#Point à 2D
Point2D=namedtuple('Point2D', ['x','y'])

p2d = Point2D(x=0,y=1)
print(p2d)

print(p2d[0])


#Point à 1D
Point1D = namedtuple("Point1D",["x"])
print(Point1D)

p_04=Point1D(0.4)
print(p_04)
p_05=Point1D(0.5)
print(p_04+p_05)

#Ce qu'on voudrait 
#p_04+p_05 == Point1D(0.9)
#(0.4,0.5)

def ajout_point1d(point1, point2):
  x = point1[0]+point2[0]
  print(x)
  return Point1D(x)

print(f"Addition ok :{ajout_point1d(p_04,p_05)} ")

def norme1d(p1):
  return (p1.x **2) **0.5

p_09=ajout_point1d(p_04,p_05)

print (norme1d(p_09))

Point2D=namedtuple('Point2D',' x y ')

p1=Point2D(0,1)
p2=Point2D(1,0)

print(p1)
print(p2)

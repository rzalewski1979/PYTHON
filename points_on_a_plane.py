import math

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.__x=float(x)
        self.__y=float(y)
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self,x,y):
        return math.hypot(abs(self.__x-x),abs(self.__y-y))
    def distance_from_point(self,point):
        self.__distance=self.distance_from_xy(point.getx(),point.gety())
        return self.__distance
point1=Point(0,0)
point2=Point(1,1)
print(point2.distance_from_xy(2,0))
print(point1.distance_from_point(point2))

class Triangle:
    def __init__(self,vertice1,vertice2,vertice3):
        self.__vertice1=vertice1.distance_from_point(vertice2)
        self.__vertice2=vertice2.distance_from_point(vertice3)
        self.__vertice3=vertice3.distance_from_point(vertice1)

    def perimeter(self):
        return self.__vertice1+self.__vertice2+self.__vertice3
triangle=Triangle(Point(0,0),Point(1,0),Point(0,1))
print(triangle.perimeter())

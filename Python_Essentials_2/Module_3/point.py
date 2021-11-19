# POINTS ON A PLANE

# Each point located on the plane can be described as a pair
# of coordinates customarily called x and y.
# The task is to create a class which stores both coordinates
# as float numbers, and the objects of this class can evaluate
# the distances between any of the two points situated on the plane.

# Requeriments:
# 1) The class is called Point.
# 2) Its constructor accepts two arguments (x and y respectively),
# both default to zero.
# 3) All the properties should be private.
# 4) The class contains two parameterless methods called getx() and gety(),
# which return each of the two coordinates (the coordinates are stored 
# privately, so they cannot be accessed directly from within the object).
# 5) The class provides a method called distance_from_xy(x,y), which calculates
# and returns the distance between the point stored inside the object and the
# other point given as a pair of floats.
# 6) The class provides a method called distance_from_point(point), which
# calculates the distance (like the previous method), but the other point's
# location is given as another Point class object.


import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        distance = math.hypot(self.__x - x, self.__y - y)
        return distance

    def distance_from_point(self, point):
        x = point.getx()
        y = point.gety()
        return self.distance_from_xy(x, y)

# Testing class
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
# TRIANGLE

# The constructor of the this class accepts three arguments
# - All of them are objects of the Point class.
# - The points are stored inside the object as a private list.
# - The class provides a parameterless method called perimeter(),
# which calculates the perimeter of the triangle described by the
# three points; the perimeter is a sum of all legs' lengths.


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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__list_of_points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        perimeter = 0
        for n, p in enumerate(self.__list_of_points):
            if n != len(self.__list_of_points) - 1:
                distance = p.distance_from_point(self.__list_of_points[n + 1])
            else:
                distance = p.distance_from_point(self.__list_of_points[0])
            perimeter += distance
        return perimeter


# Testing classes
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
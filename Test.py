"""Q1. Create a RectangleGeometry class which takes in length and breadth as initialize parameter. Make two methods getArea
 and getPerimeter inside this class. Which when invoked returns area and perimeter of each rectangle instance."""

class RectangleGeometry:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def getArea(self):
        area = self.length*self.breadth
        print(area)
    def getPerimeter(self):
        perimeter = 2*(self.length+self.breadth)
        print(perimeter)

r = RectangleGeometry(1,2)
r.getArea(), r.getPerimeter()
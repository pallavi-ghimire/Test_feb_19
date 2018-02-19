"""Q1. Create a RectangleGeometry class which takes in length and breadth as initialize parameter. Make two methods getArea
 and getPerimeter inside this class. Which when invoked returns area and perimeter of each rectangle instance."""

class RectangleGeometry:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def getArea(self):
        area = self.length*self.breadth
        return area
    def getPerimeter(self):
        perimeter = 2*(self.length+self.breadth)
        return perimeter

r = RectangleGeometry(1,2)
print(r.getArea(), r.getPerimeter())


"""Q2. Create a class Circle which has a class variable PI with the value=22/7. Make two methods getArea and getCircumference inside 
this Circle class. Which when invoked returns area and circumference of each circle instances."""
class Circle:
    PI = 22/7
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        area = Circle.PI * self.radius * self.radius
        return area
    def getCircumference(self):
        cir = Circle.PI * 2 * self.radius
        return cir

c = Circle(3)
print(c.getArea(), c.getCircumference())


"""Create a Employee class and initialize it with first_name, last_name and salary. Also, it has a derived attribute called email, which is self generated when instance is created. Now, make methods to :
      a. Display - It should display all information of the employee instance."""


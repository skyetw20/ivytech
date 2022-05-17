#Divyanshu Gupta
#SDEV 220
#Camculation of area and parameter of the triangle
#19th April 2022

import math #importing math module for handeling the various maths operation

class GeometricObject: #creating classs for handeling the color and filled status of the triangle
    def __init__(self, color="green", filled=True):  #constructor for intialising the variables for the class
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)


class Triangle(GeometricObject):  #class for handeling the various operation such as area nad parameter for the triangle
    def __init__(self, side1=2.0, side2=2.0, side3=2.0, color="green", isFilld=True): #constructor
        super().__init__(color, isFilld)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    #accessors and mutators
    def getSide1(self): 
        return self.side1

    def setSide1(self, side1):
        self.side1 = side1

    def getSide2(self):
        return self.side2

    def setSide2(self, side2):
        self.side2 = side2

    def getSide3(self):
        return self.side3

    def setSide3(self, side3):
        self.side3 = side3

    def getArea(self): #for calcualting area
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def getPerimeter(self): #for calcualting parameter of the trirangle
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return super().__str__() + " Triangle: side1 = " + str(self.side1) + " side2 = " + \
               str(self.side2) + " side3 = " + str(self.side3)


def main(): #main function for handleing the function fo the programme
    (s1,s2,s3)=(2.0,2.0,2.0)
    try:#try and except block for handeling various form of input from user
        s1, s2, s3 = eval(input("Enter three sides of a Triangle(as 3,4,5): "))
    except:

        pass
        
    color = input("Enter color of a triangle: ")
    isFilled = bool(int(input("Is the triangle filled? (1 or 0): ")))

    trngl = Triangle(s1, s2, s3, color, isFilled)
    print("Triangle's area is:", trngl.getArea())
    print("Triangle's perimeter is:", trngl.getPerimeter())
    print(trngl)


main()
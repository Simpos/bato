from math import asin,sqrt,pi



class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        if self.x == 0 and self.y == 0:
            self.angle = 0
        else:
            try:
                self.angle = asin((self.y / self.x) % (pi/2))
            except ValueError:
                print("Error", self.y / self.x)
                self.angle = 0
            except ZeroDivisionError:
                print("AAA")
                self.angle = 0

    def norme(self):
        return sqrt(self.x**2+self.y**2)

    def prod(self,val):
        return Vector(self.x*val,self.y*val)

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def getTupple(self):
        return self.x,self.y

    def getNormalized(self):
        return self.prod(1/self.norme())



from math import asin,sqrt,pi



class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = asin(self.y / self.x % pi/2)

    def norme(self):
        return sqrt(self.x**2+self.y**2)

    def produit(self,val):
        return Vector(self.x*val,self.y*val)

    def somme(self,other):
        return Vector(sefl.x+other.x,self.y+other.y)


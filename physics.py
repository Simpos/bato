from math import sqrt,log


BLACK = (0,0,0)
BLUE =  (0, 127, 255)
GREEN = (0,255,0)
RED = (255,0,0)
DARK_BLUE = (0,0,139)

rho_air = 1.204
surface = 1
cx ={

}

def calcPortance(V,angle):
    return .5 * rho_air * surface * (V ** 2) * cx[angle]

def calcTrainee(V,angle):
    return .5 * rho_air * surface * (V ** 2) * cz[angle]
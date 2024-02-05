from math import cos,sin

def prodMat(angle,x,y):
    return (cos(angle)*x-sin(angle)*y,sin(angle)*y+cos(angle)*x)

def convertion(angle):
    """ convert angle from degree to rad"""
    return angle * PI / 180

PI = 3.14
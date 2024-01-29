import pygame
from math import sqrt
from physics import *
from maf import *


SIZE = 10
COTE = sqrt(2) * SIZE

class Bateau:
    def __init__(self,x,y,vx,vy,ax,ay,angle,voile,screen):
        """
            x,y : position
            vx,vy : speed,
            ax,ay : acceleration
            angle : angle between the top of the boat and the line west
            voile : {0,1,2} on the different profile of the sail
        """
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.angle = angle
        self.voile = voile
        self.screen = screen
        self.rect = pygame.Rect(self.x,self.y,SIZE,SIZE)


    def calculateSpeed(self):
        pass

    def rotate(self,pro):
        self.angle += pro
        x,y=prodMat(self.angle,self.x+640,360+self.y)
        self.rect = pygame.Rect(x,y,SIZE,SIZE)


    def draw_boat(self):
        pygame.draw.rect(self.screen,BLACK,self.rect)
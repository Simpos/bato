import pygame
from math import sqrt
from vector import *
from physics import *
from maf import *


SIZE = 10
COTE = sqrt(2) * SIZE

class Bateau:
    def __init__(self,x,y,vx,vy,ax,ay,angle):
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
        self.surface = pygame.Surface((SIZE,SIZE),pygame.SRCALPHA)
        self.surface.fill(BLACK)
        self.rotated_surface = self.surface
        self.rect = self.surface.get_rect()
        self.profilVoile = [1,2,3]
        self.actifProfilVoile = 0
        self.direction = Vector(self.vx,self.vy)

    def calculateSpeed(self):
        pass

    def rotate(self,pro):
        self.angle += pro
        #SURFACE
        self.rotated_surface = pygame.transform.rotate(self.surface,self.angle)
        self.rect = self.rotated_surface.get_rect(center = (self.x,self.y))
        #DIRECTION
        norme = self.direction.norme()
        angles = convertion(self.direction.angle + self.angle)
        new = Vector(cos(angles),sin(angles))
        self.direction = new.prod(norme)

    def changeVoile(self,direct:bool):
        if direct:
            if self.actifProfilVoile < len(self.profilVoile):
                self.actifProfilVoile += 1
        else:
            if self.actifProfilVoile > 0:
                self.profilVoile -= 1

    def __repr__(self):
        return f"{self.x} {self.y}"
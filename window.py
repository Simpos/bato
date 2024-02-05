import pygame
from sail import Bateau
from vind import Wind
from vector import Vector
from physics import *


t = 0


W,H = 1280,720


pygame.init()
screen = pygame.display.set_mode((1280, 720))


clock = pygame.time.Clock()
running = True


boat = Bateau(W//2,H//2,20,20,0,0,0)

def drawVect(vect,point):
    new = Vector(point[0],point[1]) + vect
    pygame.draw.line(screen,RED,point,new.getTupple())


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(boat)
            if event.key == pygame.K_LEFT:
                boat.rotate(22.5)
                print(boat.angle)
            elif event.key == pygame.K_RIGHT:
                boat.rotate(-22.5)
            elif event.key == pygame.K_UP:
                boat.changeVoile(True)
            elif event.key == pygame.K_DOWN:
                boat.changeVoile(False)

    screen.fill(BLUE)

    drawVect(boat.direction,(boat.x,boat.y))
    screen.blit(boat.rotated_surface,(boat.rect.x,boat.rect.y))
    pygame.display.update()

    t += 1
    clock.tick(60)

pygame.quit()
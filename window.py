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


boat = Bateau(0,0,0,0,0,0,0,0,screen)





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            boat.rotate(-15)
        elif event.type == pygame.KEYDOWN:
            boat.rotate(15)


    screen.fill(BLUE)
    boat.draw_boat()
    pygame.display.flip()

    t += 1
    clock.tick(60)

pygame.quit()
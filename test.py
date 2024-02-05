import sys, pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((200, 200))
CLOCK  = pygame.time.Clock()

surface = pygame.Surface((50 , 50), pygame.SRCALPHA)
surface.fill((0, 0, 0))
rotated_surface = surface
rect = surface.get_rect()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((255, 255, 255))
    """
    angle -= 89.9
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect(center = (100, 100))
    SCREEN.blit(rotated_surface, (rect.x, rect.y))
    """
    pygame.draw.polygon(SCREEN, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
    pygame.display.update()
    CLOCK.tick(30)
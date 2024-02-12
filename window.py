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


boat = Bateau(W//2,H//2,0,0,0,0,0)
wind = Wind(1,1)

def drawVect(vect,point,color=RED,size=1):
    new = Vector(point[0],point[1]) + vect
    pygame.draw.line(screen,color,point,new.getTupple(),width=size)

def draw_arrow(
        surface: pygame.Surface,
        start: pygame.Vector2,
        direction: Vector,
        color: pygame.Color,
        body_width: int = 2,
        head_width: int = 4,
        head_height: int = 2,
    ):
    """Draw an arrow between start and end with the arrow head at the end.

    Args:
        surface (pygame.Surface): The surface to draw on
        start (pygame.Vector2): Start position
        end (pygame.Vector2): End position
        color (pygame.Color): Color of the arrow
        body_width (int, optional): Defaults to 2.
        head_width (int, optional): Defaults to 4.
        head_height (float, optional): Defaults to 2.
    """
    endd = direction + Vector(start[0],start[1])
    end = pygame.Vector2(endd.x,endd.y)
    arrow = start - end
    angle = arrow.angle_to(pygame.Vector2(0, -1))
    body_length = arrow.length() - head_height

    # Create the triangle head around the origin
    head_verts = [
        pygame.Vector2(0, head_height / 2),  # Center
        pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
        pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
    ]
    # Rotate and translate the head into place
    translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
    for i in range(len(head_verts)):
        head_verts[i].rotate_ip(-angle)
        head_verts[i] += translation
        head_verts[i] += start

    pygame.draw.polygon(surface, color, head_verts)

    # Stop weird shapes when the arrow is shorter than arrow head
    if arrow.length() >= head_height:
        # Calculate the body rect, rotate and translate into place
        body_verts = [
            pygame.Vector2(-body_width / 2, body_length / 2),  # Topleft
            pygame.Vector2(body_width / 2, body_length / 2),  # Topright
            pygame.Vector2(body_width / 2, -body_length / 2),  # Bottomright
            pygame.Vector2(-body_width / 2, -body_length / 2),  # Bottomleft
        ]
        translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
        for i in range(len(body_verts)):
            body_verts[i].rotate_ip(-angle)
            body_verts[i] += translation
            body_verts[i] += start

        pygame.draw.polygon(surface, color, body_verts)

actif = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            actif = True
            print(boat)
            if event.key == pygame.K_LEFT:
                boat.rotate(-22.5)
                print(boat.angle)
            elif event.key == pygame.K_RIGHT:
                boat.rotate(22.5)
            elif event.key == pygame.K_UP:
                boat.changeVoile(True)
            elif event.key == pygame.K_DOWN:
                boat.changeVoile(False)
            elif event.key == pygame.K_SPACE:
                boat.speedUpdate(1,0)
            elif event.key == pygame.K_t:
                boat.update(relative_speed)

    relative_speed = boat.direction.prod(-1) + wind


    screen.fill(BLUE)

    #Draw Vector
    #drawVect(wind,(1200,650),DARK_BLUE,10)
    drawVect(boat.direction.prod(20),(boat.x,boat.y))
    drawVect(relative_speed.prod(20),(boat.x,boat.y),GREEN)
    draw_arrow(screen, (1200,650),wind.prod(20) ,pygame.Color("dodgerblue"), 10, 20, 12)

    screen.blit(boat.rotated_surface,(boat.rect.x,boat.rect.y))
    pygame.display.update()
    if actif and t == 30:
        boat.update(relative_speed)
        t = 0
    t += 1
    clock.tick(60)

pygame.quit()
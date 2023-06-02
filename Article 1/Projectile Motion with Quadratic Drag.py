import pygame
import pymunk
from pymunk import pygame_util
import sys
#UPWARDS --> -y, RIGHT --> +x, TOP LEFT = (0, 0,)
pygame.init()
window = pygame.display.set_mode((1400, 700))
width = 1400
height = 700
def draw(space, window, DrawOptions):
    space.debug_draw(DrawOptions)
    pygame.display.update()

def projectile(space, color):
    body = pymunk.Body(body_type = pymunk.Body.DYNAMIC)
    body.position = (0, height)
    proj = pymunk.Circle(body, radius = 1.0)
    proj.mass = 1
    proj.color = color
    space.add(body, proj)
    return proj

def run(window, width, height):
    run = True
    t = pygame.time.Clock()
    dt = 0.001
    pygame.display.set_caption('Projectile Motion with Quadratic Drag')
    space = pymunk.Space()
    space.gravity = (0, 9.81)
    draw_options = pygame_util.DrawOptions(window)

    projno = projectile(space, (255, 255, 255, 100))
    projno.body.apply_impulse_at_local_point((70, -100), (0, 0))
    projquad = projectile(space, (0, 255, 0, 100))
    projquad.body.apply_impulse_at_local_point((70, -100), (0, 0))
    
    for i in range(width):#
        if i%100==0:
            pygame.draw.line(window, (0, 0, 255), (i, 0), (i, height))
    
    for i in range(height):
        v = height-i
        if v%100==0:
            pygame.draw.line(window, (255, 0, 0), (0, v), (width, v))
        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        projquad.body.apply_force_at_local_point(-abs(projquad.body.velocity)*projquad.body.velocity*0.01, (0, 0))

        draw(space, window, draw_options)
        space.step(dt)
        t.tick(1/dt)
    pygame.quit()
if __name__ == "__main__":
    run(window, width, height)
#python 'C:\Users\swaagat\Desktop\WA3 Sims\Projectile Motion.py'
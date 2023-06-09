import pygame
import pymunk
from pymunk import pygame_util
import matplotlib.pyplot as plt
import sys
#UPWARDS --> -y, RIGHT --> +x, TOP LEFT = (0, 0,)
pygame.init()
window = pygame.display.set_mode((1440, 700))
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

x_ax=[]
y_i = []
y_r = []
def run(window, width, height):
    run = True
    t = pygame.time.Clock()
    dt = 0.001
    pygame.display.set_caption('Projectile Motion with Linear Drag')
    space = pymunk.Space();
    space.gravity = (0, 9.81)
    draw_options = pygame_util.DrawOptions(window)

    projno = projectile(space, (255, 255, 255, 100))
    projno.body.apply_impulse_at_local_point((60, -100), (0, 0))
    projlin = projectile(space, (0, 255, 0, 100))
    projlin.body.apply_impulse_at_local_point((60, -100), (0, 0))
    
    for i in range(width):#
        if i%100==0:
            pygame.draw.line(window, (0, 0, 255), (i, 0), (i, height))
    
    for i in range(height):
        v = height-i
        if v%100==0:
            pygame.draw.line(window, (255, 0, 0), (0, v), (width, v))
    T=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        projlin.body.apply_force_at_local_point(-projlin.body.velocity*0.1, (0, 0))

        draw(space, window, draw_options)
        space.step(dt)
        t.tick(1/dt)
        x_ax.append(T)
        y_i.append(projno.body.position.dot((0, 1)))
        y_r.append(-projlin.body.velocity.dot((0, 1)))
        T += dt
        if T>=120:
            run=False
    plt.plot(x_ax, y_r)
    plt.show()
    pygame.quit()
if __name__ == "__main__":
    run(window, width, height)
#python 'C:\Users\swaagat\Desktop\WA3 Sims\Projectile Motion.py'
import pygame
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Object import *
from Transform import *

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

pygame.display.set_caption('OpenGL in Python')
mesh = Cube(GL_POLYGON, "../images/blocks.tif")
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -3)
glEnable(GL_DEPTH_TEST)

objects = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, -1)))
cube.add_component(Cube(GL_POLYGON, "../images/blocks.tif"))

cube2 = Object("Cube2")
cube2.add_component(Transform((0, 1, 0)))
cube2.add_component(Cube(GL_POLYGON, "../images/blocks.tif"))

objects.append(cube)
objects.append(cube2)

glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 0, 0, 1))
glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))

clock = pygame.time.Clock()
fps = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5,1,0,1)

    for o in objects:
        o.update()
    pygame.display.flip()
    clock.tick(fps)
    #pygame.time.wait(100)
pygame.quit()
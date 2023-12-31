import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
timesClicked = 0


def plot_line_old(p1, p2): # ploting points
    if p2[0] < p1[0]:
        temp = p2
        p2 = p1
        p1 = temp

    x0, y0 = p1
    x1, y1 = p2

    m = (y1 - y0) / (x1 - x0)
    c = y0 - (m * x0)
    for x in range(x0, x1):
        y = m * x + c  # LINE EQUATION
        screen.set_at((int(x), int(y)), white)


def plot_line(p1, p2): # bresenham's line algorithm
    x0, y0 = p1
    x1, y1 = p2
    dx = abs(x1 - x0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    dy = -abs(y1 - y0)
    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx + dy

    while True:
        screen.set_at((x0, y0), white)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if timesClicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            timesClicked += 1
            if timesClicked > 1:
                # pygame.draw.line(screen, white, point1, point2, 1) # old method
                plot_line(point1, point2)  # new method
                timesClicked = 0
    pygame.display.update()
pygame.quit()

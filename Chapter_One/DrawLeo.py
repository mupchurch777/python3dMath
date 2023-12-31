import pygame

pygame.init()
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)


def draw_star(x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_star(121, 320, 15)
    draw_star(327, 324, 15)
    draw_star(691, 431, 20)
    draw_star(697, 317, 10)
    draw_star(626, 246, 30)
    draw_star(343, 212, 10)
    draw_star(653, 165, 10)
    draw_star(773, 102, 10)
    draw_star(822, 153, 10)
    pygame.display.update()
pygame.quit()
import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)


def to_pygame_coordinates(display, x, y):
    return x, display.get_height() - y


screen.set_at(to_pygame_coordinates(screen, 100, 100), white)
screen.set_at(to_pygame_coordinates(screen, 200, 200), white)
pygame.display.update()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.display.update()
pygame.quit()

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (217, 217, 217), (0, 0, 500, 500), 0)
circle(screen, (225, 255, 0), (250, 250), 125)
circle(screen, (0, 0, 0), (250, 250), 125, 2)
rect(screen, (0, 0, 0), (185, 315, 130, 25), 0)
circle(screen, (225, 0, 0), (185, 225), 25, 15)
circle(screen, (0, 0, 0), (185, 225), 10, 0)
circle(screen, (0, 0, 0), (185, 225), 25, 1)
circle(screen, (225, 0, 0), (315, 225), 20, 10)
circle(screen, (0, 0, 0), (315, 225), 10, 0)
circle(screen, (0, 0, 0), (315, 225), 20, 1)
polygon(screen, (0, 0, 0), [(121, 158), (128, 147),
                            (227, 210), (221, 220)])
polygon(screen, (0, 0, 0), [(272, 210), (372, 171),
                            (376, 182), (277, 219)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

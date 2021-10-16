import pygame
from pygame.draw import *
from random import randint
pygame.init()
FPS = 30
screen = pygame.display.set_mode((900, 500))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    '''
    функция рисует шарик и задаёт ему скорость, цвет и размер
    '''

    def __init__(self):
        '''
        задаёт параметры шарика указанные выше
        '''
        self.x = randint(100, 900)
        self.y = randint(100, 500)
        self.r = randint(10, 20)
        self.vx = randint(-4, 4)
        self.vy = randint(-4, 4)
        self.color = COLORS[randint(0, 5)]

    def spawn(self):
        '''
        рисует сам шарик
        '''
        circle(screen, self.color, (self.x, self.y), self.r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
a = []
s = 0
quantity = randint(20, 100)
for i in range(quantity):
    a.append(Ball())
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
    for i in range(0, len(a)):
        a[i].x += a[i].vx
        a[i].y += a[i].vy
        if a[i].x > 900 or a[i].x < 0:
            a[i].vx = -a[i].vx
        if a[i].y > 500 or a[i].y < 0:
            a[i].vy = -a[i].vy
        a[i].spawn()
    text = pygame.font.SysFont('arial', 24)
    s_sum = 'Total' + str(s)
    sc_text = text.render(s_sum, 1, GREEN)
    pos = sc_text.get_rect(topleft=(0, 0))
    screen.blit(sc_text, pos)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1 = event.pos[0]
            y1 = event.pos[1]
            for i in range(len(a)-1, -1, -1):
                if (x1 - a[i].x) ** 2 + (y1 - a[i].y) ** 2 <= a[i].r ** 2:
                    s += 1
                    a.pop(i)
    pygame.display.update()
pygame.quit()

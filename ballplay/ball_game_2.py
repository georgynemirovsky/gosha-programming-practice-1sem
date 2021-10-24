import pygame
import json
from pygame.draw import *
from random import randint
pygame.init()
FPS = 60
screen = pygame.display.set_mode((900, 500))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
t = 0


def draw_ellipse_angle(surface, color, rect, angle, width=0):
    '''
    функция поворачивает эллипс
    '''
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(
        center=target_rect.center))


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
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)
        self.color = COLORS[randint(0, 5)]

    def spawn(self):
        '''
        рисует сам шарик
        '''
        circle(screen, self.color, (self.x, self.y), self.r)


class rectangle:
    '''
    функция рисует эллипс и задаёт ему скорость, цвет и размер
    '''

    def __init__(self):
        '''
        задаёт параметры эллипса указанные выше
        '''
        self.x = randint(100, 900)
        self.y = randint(100, 500)
        self.lx = randint(25, 50)
        self.ly = randint(25, 50)
        self.vx = randint(-2, 2)
        self.vy = randint(-2, 2)
        self.color = COLORS[randint(0, 5)]

    def spawn(self, angle):
        '''
        рисует эллипс по заданым координатам и с определённым цветом
        '''
        draw_ellipse_angle(screen, self.color, [
                           self.x, self.y, self.lx, self.ly], angle)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
a = []
b = []
score = 0
for i in range(50):
    a.append(Ball())
for i in range(50):
    b.append(rectangle())
time = 0
while not finished and time <= 60 and len(a) + len(b) != 0:
    time += 1/FPS
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
    for i in range(0, len(b)):
        b[i].x += b[i].vx
        b[i].y += b[i].vy
        if b[i].x > 900 or b[i].x < 0:
            b[i].vx = -b[i].vx
        if b[i].y > 500 or b[i].y < 0:
            b[i].vy = -b[i].vy
        t += 0.1
        b[i].spawn(t)
    text = pygame.font.SysFont('arial', 24)
    s_sum = 'Total' + str(score)
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
                    score += 1
                    a.pop(i)
            for i in range(len(b)-1, -1, -1):
                if abs(b[i].x + b[i].lx / 2 - x1) <= b[i].lx / 2 and abs(b[i].y + b[i].ly / 2 - y1) <= b[i].ly / 2:
                    score += 2
                    b.pop(i)
    pygame.display.update()
with open(r'waste_time.json', 'r') as f:
    data = json.load(f)
print('enter your name')
name = input()
flag = False
for a, b in data.items():
    if a == name:
        flag = True
        if score > b:
            data[name] = score
if not(flag):
    data[name] = score
with open(r'waste_time.json', 'w') as f:
    json.dump(data, f)
with open(r'waste_time.json', 'r') as f:
    data = json.load(f)
c = 0
finished = False
while not finished:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    for a, b in data.items():
        i = str(a) + ' = ' + str(b)
        text = pygame.font.SysFont('arial', 24)
        sc_text = text.render(i, 1, GREEN)
        pos = sc_text.get_rect(topleft=(450, c * 48))
        screen.blit(sc_text, pos)
        c += 1
    pygame.display.update()
    c = 0
pygame.quit()

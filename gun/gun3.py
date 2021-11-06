import math
from random import choice
import random
import pygame
from pygame.draw import *
FPS = 30
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 800
HEIGHT = 600

class Arrow:
    def __init__(self, screen: pygame.Surface, x, y, j):
        '''генирирует потроны в форме треугольника'''
        self.screen = screen
        self.x = x + j * 30
        self.y = y
        self.r = 0
        self.vx = j * 0.2
        self.vy = 0
        self.j = j
        self.color = choice(GAME_COLORS)
        self.shoot_time = pygame.time.get_ticks()

    def move(self):
        '''перемещние треугольника'''
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        '''рисует треугольник'''
        polygon(self.screen, self.color, ((self.x, self.y - 5),
                (self.x, self.y + 5), (self.x + self.j * 10, self.y)))
class Gun:
    def __init__(self, screen, x, y, j):
        '''параметры пушки'''
        self.screen = screen
        self.an = 1
        self.color = GREEN
        self.x = x
        self.y = y 
        self.j = j
        self.life = 5


    def fire1_end(self, event):
        """
        Выстрел треугольником
        Происходит при отпускании кнопки мыши.
        """
        global arrowes, bullet
        bullet += 1
        new_arrow = Arrow(self.screen, self.x, self.y, self.j)
        arrowes.append(new_arrow)

    def draw(self):
        '''рисует пушку'''
        polygon(self.screen, self.color, ((self.x, self.y), (40 * self.j + self.x, self.y)), width=5)
        circle(self.screen, self.color, (self.x, self.y), 10)
        polygon(self.screen, self.color, ((self.x - 20, self.y), (self.x + 20,
                self.y), (self.x + 10, self.y + 10), (self.x - 10, self.y + 10)))
    def move(self):
        '''рперемещние треугольника'''
        self.x += self.vx
        self.y -= self.vy

    def hit(self, obj):
        '''проверяет столкновение пушки с треугольником'''
        if abs(self.x - obj.x) <= 10 and abs(self.y - obj.y) <= 10:
            return True
        return False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
arrowes = []
balls = []
clock = pygame.time.Clock()
finished = False
gun1 = Gun(screen, 20, 450, 1)
gun2 = Gun(screen, 780, 450, -1)
while not finished:
    screen.fill(WHITE)
    gun1.draw()
    gun2.draw()
    for i in arrowes:
        i.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            gun1.fire1_end(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            gun2.fire1_end(event)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        gun1.x -= 0.1
    elif keys[pygame.K_d]:
        gun1.x += 0.1
    elif keys[pygame.K_w]:
        gun1.y -= 0.1
    elif keys[pygame.K_s]:
        gun1.y += 0.1
    if keys[pygame.K_j]:
        gun2.x -= 0.1
    elif keys[pygame.K_l]:
        gun2.x += 0.1
    elif keys[pygame.K_i]:
        gun2.y -= 0.1
    elif keys[pygame.K_k]:
        gun2.y += 0.1
    for i in arrowes:
        i.move()
    for i in arrowes[::-1]:
        if gun1.hit(i):
            gun1.life -= 1
            arrowes.remove(i)
            if gun1.life == 0:
                finished = True
                flag = True
        elif gun2.hit(i):
            arrowes.remove(i)
            gun2.life -= 1
            if gun2.life == 0:
                finished = True
                flag = False
finished = False
while not finished:
        screen.fill(WHITE)
        text = pygame.font.SysFont('arial', 24)
        if flag:
            i = 'игрок слева - лох'
        else:
            i = 'игрок справа - лох'
        sc_text = text.render(i, 1, GREEN)
        pos = sc_text.get_rect(center = (400, 300))
        screen.blit(sc_text, pos)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
pygame.quit()
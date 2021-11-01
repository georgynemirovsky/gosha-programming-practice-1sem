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


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.shoot_time = pygame.time.get_ticks()

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx/2
            if self.x + self.r > 800:
                self.x = 790
            else:
                self.x = 10
        if self.y + self.r >= 600:
            self.vy = -self.vy/1.5
            self.vx = self.vx/1.5
            self.y = 590
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 1

    def draw(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2 and obj.r != 0) \
           or (obj.a != 0 and (abs(self.x - (obj.x + obj.a / 2)) <= self.r + obj.a / 2)
           and (abs(self.y - (obj.y + obj.b / 2)) <= self.r + obj.b / 2)):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-450), (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        line(screen, self.color, (20, 450), (math.cos(self.an) *
             self.f2_power + 20, math.sin(self.an) * self.f2_power + 450), width=5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREEN


class target:
    def __init__(self, screen, point):
        """ Инициализация новой цели круг. """
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(10, 50)
        self.a = 0
        self.b = 0
        self.color = RED
        self.screen = screen
        self.points = point

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)


class target_rect(target):
    def __init__(self, screen, point):
        """ Инициализация новой цели прямоугольник. """
        self.vy = 5
        self.a = random.randint(30, 50)
        self.b = random.randint(30, 50)
        self.color = GREEN
        self.screen = screen
        self.points = point
        self.x = random.randint(600, 780)
        self.y = -self.b
        self.r = 0

    def draw_rect(self):
        rect(self.screen, self.color, (self.x, self.y, self.a, self.b))

    def move(self):
        self.y += self.vy
        if self.y >= 600:
            self.y = -self.b


class target_ellipse(target):
    def __init__(self, screen, point):
        """ Инициализация новой цели эллипс. """
        self.vx = 5
        self.a = random.randint(30, 50)
        self.b = random.randint(30, 50)
        self.color = BLUE
        self.screen = screen
        self.points = point
        self.x = -self.a
        self.y = random.randint(40, 100)
        self.r = 0

    def draw_ellipse(self):
        ellipse(self.screen, self.color, (self.x, self.y, self.a, self.b))

    def move(self):
        self.x += self.vx
        if self.x >= 800:
            self.x = -self.b


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = target(screen, 0)
target2 = target_rect(screen, 0)
target3 = target_ellipse(screen, 0)
finished = False
while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw_rect()
    target3.draw_ellipse()
    for b in balls:
        b.draw()
    text = pygame.font.SysFont('arial', 24)
    s_sum = 'Total ' + str(target1.points + target2.points + target3.points)
    sc_text = text.render(s_sum, 1, GREEN)
    pos = sc_text.get_rect(topleft=(0, 0))
    screen.blit(sc_text, pos)
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for b in balls:
        if b.hittest(target1):
            target1.hit()
            point = target1.points
            screen_bullets = pygame.time.get_ticks()
            screen_bullets1 = pygame.time.get_ticks()
            while screen_bullets1 - screen_bullets <= 2000:
                screen.fill(WHITE)
                target1 = target(screen, point)
                s_sum = 'BULLETS ' + str(bullet)
                sc_text = text.render(s_sum, 1, RED)
                pos = sc_text.get_rect(center=(400, 300))
                screen.blit(sc_text, pos)
                pygame.display.update()
                screen_bullets1 = pygame.time.get_ticks()
            bullet = 0
            target1.draw()
        if b.hittest(target2):
            target2.hit()
            point = target2.points
            target2 = target_rect(screen, point)
            screen_bullets = pygame.time.get_ticks()
            screen_bullets1 = pygame.time.get_ticks()
            while screen_bullets1 - screen_bullets <= 2000:
                screen.fill(WHITE)
                target1 = target(screen, point)
                s_sum = 'BULLETS ' + str(bullet)
                sc_text = text.render(s_sum, 1, RED)
                pos = sc_text.get_rect(center=(400, 300))
                screen.blit(sc_text, pos)
                pygame.display.update()
                screen_bullets1 = pygame.time.get_ticks()
            bullet = 0
            target2.draw_rect()
        if b.hittest(target3):
            target3.hit()
            point = target3.points
            target3 = target_ellipse(screen, point)
            screen_bullets = pygame.time.get_ticks()
            screen_bullets1 = pygame.time.get_ticks()
            while screen_bullets1 - screen_bullets <= 2000:
                screen.fill(WHITE)
                target1 = target(screen, point)
                s_sum = 'BULLETS ' + str(bullet)
                sc_text = text.render(s_sum, 1, RED)
                pos = sc_text.get_rect(center=(400, 300))
                screen.blit(sc_text, pos)
                pygame.display.update()
                screen_bullets1 = pygame.time.get_ticks()
            bullet = 0
            target3.draw_ellipse()
        b.move()
        if time_to_die - b.shoot_time > 5000:
            balls.remove(b)
    time_to_die = pygame.time.get_ticks()
    target2.move()
    target3.move()
    gun.power_up()
pygame.quit()

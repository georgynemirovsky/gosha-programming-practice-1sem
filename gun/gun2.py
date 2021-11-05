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
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
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
        '''рисует мяч по заданным параметрам'''
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


class Arrow:
    def __init__(self, screen: pygame.Surface, x, y):
        '''генирирует потроны в форме треугольника'''
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 0
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.shoot_time = pygame.time.get_ticks()

    def move(self):
        '''рперемещние треугольника'''
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        '''рисует стрелу'''
        polygon(self.screen, self.color, ((self.x, self.y-5),
                (self.x, self.y + 5), (self.x + 10, self.y)))

    def hittest(self, obj):
        '''проверка попадания'''
        if self.x + 10 <= obj.c and self.x + 10 >= obj.a and self.y >= obj.b and self.y <= obj.d:
            return True
        False


class Gun:
    def __init__(self, screen):
        '''параметры пушки'''
        self.screen = screen
        self.f2_power = 20
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450

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
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 20

    def fire1_end(self, event):
        """
        Выстрел треугольником
        Происходит при отпускании кнопки мыши.
        """
        global arrowes, bullet
        bullet += 1
        new_arrow = Arrow(self.screen, self.x, self.y)
        self.an = math.atan2(
            (event.pos[1]-new_arrow.y), (event.pos[0]-new_arrow.x))
        new_arrow.vx = self.f2_power * math.cos(self.an)
        new_arrow.vy = - self.f2_power * math.sin(self.an)
        arrowes.append(new_arrow)
        self.f2_on = 0
        self.f2_power = 20

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREEN

    def draw(self):
        '''рисует пушку'''
        polygon(self.screen, self.color, ((self.x, self.y), (math.cos(self.an) *
                                                             self.f2_power + self.x, math.sin(self.an) * self.f2_power + self.y)), width=5)
        circle(self.screen, self.color, (self.x, self.y), 10)
        polygon(self.screen, self.color, ((self.x - 20, self.y), (self.x + 20,
                self.y), (self.x + 10, self.y + 10), (self.x - 10, self.y + 10)))

    def power_up(self):
        '''сила выстрела'''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREEN


class target:
    def __init__(self, screen, point):
        """ Инициализация новой цели. """
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
        '''Рисование новой цели'''
        circle(self.screen, self.color, (self.x, self.y), self.r)


class target_rect(target):
    def __init__(self, screen, point):
        '''инициализация прямоугольник'''
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
        '''рисование прямоугольник'''
        rect(self.screen, self.color, (self.x, self.y, self.a, self.b))

    def move(self):
        '''движение прямоугольника'''
        self.y += self.vy
        if self.y >= 600:
            self.y = -self.b


class target_ellipse(target):
    def __init__(self, screen, point):
        '''генерация эллипса'''
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
        '''рисование элллипса'''
        ellipse(self.screen, self.color, (self.x, self.y, self.a, self.b))

    def move(self):
        '''движение эллипса'''
        self.x += self.vx
        if self.x >= 800:
            self.x = -self.b


class target_dababy(target):
    def __init__(self, screen, point, x, y):
        '''генерация дабэйби'''
        self.x = x
        self.y = y
        self.vx = 3
        self.vy = 3
        self.screen = screen
        self.an = 1
        self.life = 10
        self.points = point

    def move(self, obj):
        '''движение дабэйби'''
        self.an = math.atan2((self.y - obj.y), (obj.x - self.x))
        self.vx = 2.5 * math.cos(self.an)
        self.vy = 2.5 * math.sin(self.an)
        self.x += self.vx
        self.y -= self.vy

    def draw(self, size):
        '''рисование цели зависит от размера параметр: size сжатие исходной квартиры'''
        self.dababy_surf = pygame.image.load(
            r'dababy.png')
        self.dababy_surf = pygame.transform.rotozoom(self.dababy_surf, 0, size)
        self.dababy_rect = self.dababy_surf.get_rect(center=(self.x, self.y))
        (self.a, self.b) = self.dababy_rect.topleft
        (self.c, self.d) = self.dababy_rect.bottomright
        self.screen.blit(self.dababy_surf, self.dababy_rect)

    def dababy_life(self):
        '''жизнь'''
        self.life -= 1

    def die(self, obj):
        '''прописывает смерть'''
        if (self.a - 10 < obj.x < self.c + 10) and (self.b - 10 < obj.y < self.d + 10):
            return True
        return False


class shoot_dababy(target_dababy):
    def __init__(self, screen, obj, pol, side):
        '''машина генерация'''
        self.x = obj.x
        self.y = obj.y
        self.vx = 0
        self.vy = 0
        self.pol = 1
        self.side = side
        self.screen = screen
        if pol == 'right':
            self.pol = 0

    def draw(self, size):
        '''машина рисование'''
        self.shoot_surf = pygame.image.load(
            r'lessgo.jpg')
        self.shoot_surf = pygame.transform.rotozoom(self.shoot_surf, 0, size)
        self.shoot_surf = pygame.transform.flip(self.shoot_surf, self.pol, 0)
        self.shoot_rect = self.shoot_surf.get_rect(center=(self.x, self.y))
        (self.a, self.b) = self.shoot_rect.topleft
        (self.c, self.d) = self.shoot_rect.bottomright
        self.screen.blit(self.shoot_surf, self.shoot_rect)

    def move(self):
        '''машина движение'''
        if self.side == 'tl':
            self.vx = -10
            self.vy = -10
        elif self.side == 'bl':
            self.vx = -10
            self.vy = 10
        elif self.side == 'tr':
            self.vx = 10
            self.vy = -10
        elif self.side == 'br':
            self.vx = 10
            self.vy = 10
        self.x += self.vx
        self.y += self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
arrowes = []
balls = []
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = target(screen, 0)
target2 = target_rect(screen, 0)
target3 = target_ellipse(screen, 0)
target4 = target_dababy(screen, 0, random.randint(
    100, 700), random.randint(100, 500))
shoot_time = pygame.time.get_ticks()
cartridges = []
target_small = []
finished = False
text_time = pygame.time.get_ticks()
while not finished:
    screen.fill(WHITE)
    text = pygame.font.SysFont('arial', 24)
    text_ruc = []
    text_ruc.append('Небольшое руководство:')
    text_ruc.append(
        '- очки начисляютя только за самих Dababy (убить можно 10 раз попав в мишень)')
    text_ruc.append('- убить Dababy можно только треугольниками (ПКМ)')
    text_ruc.append('- есть второй тип снарядов, имеющих гравитацию (ЛКМ)')
    text_ruc.append('(нужны для поражения простых мешений)')
    text_ruc.append('- простые мешени убить не могут, но дают очки')
    text_ruc.append('- попытка выхода за экран или налёт на Dababy - поражение')
    text_ruc.append('- управление стрелками')
    text_ruc.append('- закрытие руководства - крестик или подождать минуту')
    for i in text_ruc:
        sc_text = text.render(i, 1, GREEN)
        pos = sc_text.get_rect(topleft=(10, text_ruc.index(i)*32))
        screen.blit(sc_text, pos)

    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    text_time1 = pygame.time.get_ticks()
    if text_time1 - text_time >= 60000:
        finished = True
finished = False
while not finished:
    screen.fill(WHITE)
    target1.draw()
    target2.draw_rect()
    target3.draw_ellipse()
    target4.draw(0.1)
    for i in cartridges:
        i.draw(0.1)
    for i in target_small:
        i.draw(0.05)
    for b in balls:
        b.draw()
    for a in arrowes:
        a.draw()
    gun.draw()
    text = pygame.font.SysFont('arial', 24)
    s_sum = 'Total ' + str(target1.points + target2.points +
                           target3.points + target4.points)
    sc_text = text.render(s_sum, 1, GREEN)
    pos = sc_text.get_rect(topleft=(0, 0))
    screen.blit(sc_text, pos)
    flag = False
    for i in cartridges:
        if i.die(gun):
            flag = True
            break
    for i in target_small:
        if i.die(gun):
            flag = True
            break
    if 10 >= gun.x or gun.x >= 790 or gun.y >= 590 or gun.y <= 10:
        flag = True
    if target4.die(gun) or flag:
        finished = True
        flag = True
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            gun.fire1_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gun.x -= 5
    elif keys[pygame.K_RIGHT]:
        gun.x += 5
    elif keys[pygame.K_UP]:
        gun.y -= 5
    elif keys[pygame.K_DOWN]:
        gun.y += 5
    for b in balls:
        if b.hittest(target1):
            target1.hit()
            point = target1.points
            target1 = target(screen, point)
            screen_bullets = pygame.time.get_ticks()
            screen_bullets1 = pygame.time.get_ticks()
            bullet = 0
            target1.draw()
        if b.hittest(target2):
            target2.hit()
            point = target2.points
            target2 = target_rect(screen, point)
            screen_bullets = pygame.time.get_ticks()
            screen_bullets1 = pygame.time.get_ticks()
            bullet = 0
            target2.draw_rect()
        if b.hittest(target3):
            target3.hit()
            point = target3.points
            target3 = target_ellipse(screen, point)
            screen_bullets = pygame.time.get_ticks()
            screen_bullets1 = pygame.time.get_ticks()
            bullet = 0
            target3.draw_ellipse()
        b.move()
        if time_to_die - b.shoot_time > 1000:
            balls.remove(b)
    for a in arrowes[::-1]:
        a.move()
        if a.hittest(target4):
            target4.dababy_life()
            arrowes.remove(a)
            point = target4.points
            if target4.life == 0:
                for i in range(10):
                    target4.hit()
                point = target4.points
                target_small.append(target_dababy(
                    screen, point, target4.x + 40, target4.y + 40))
                target_small.append(target_dababy(
                    screen, point, target4.x - 40, target4.y + 40))
                target_small.append(target_dababy(
                    screen, point, target4.x - 40, target4.y - 40))
                target_small.append(target_dababy(
                    screen, point, target4.x + 40, target4.y - 40))
                for i in target_small:
                    i.draw(0.05)
                target4 = target_dababy(screen, point, random.randint(
                    100, 700), random.randint(100, 500))
                shoot_time = pygame.time.get_ticks()
                bullet = 0
                target4.draw(0.1)
                pygame.display.update()
            break
        if len(target_small) != 0:
            for i in target_small[::-1]:
                if a.hittest(i):
                    i.life -= 2
                    if i.life == 0:
                        target_small.remove(i)
                    arrowes.remove(a)
                    break
    time_to_die = pygame.time.get_ticks()
    if time_to_die - shoot_time >= 2000:
        cartridges = []
        shoot_time = pygame.time.get_ticks()
        cartridges.append(shoot_dababy(screen, target4, 'left', 'tl'))
        cartridges.append(shoot_dababy(screen, target4, 'left', 'bl'))
        cartridges.append(shoot_dababy(screen, target4, 'right', 'tr'))
        cartridges.append(shoot_dababy(screen, target4, 'right', 'br'))
    target2.move()
    target3.move()
    target4.move(gun)
    for i in cartridges:
        i.move()
    for i in target_small:
        i.move(gun)
    gun.power_up()
finished = False
if flag:
    while not finished:
        screen.fill(WHITE)
        big_surf = pygame.image.load(
            r'lessgo.jpg')
        big_rect = big_surf.get_rect(topleft=(0, 0))
        big_surf = pygame.transform.rotozoom(big_surf, 0, 1.3)
        screen.blit(big_surf, big_rect)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
pygame.quit()

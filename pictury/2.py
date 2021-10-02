import pygame
from pygame.draw import *


def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(
        center=target_rect.center))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((793, 1123))
# начало кота
cat_color = (200, 113, 55)
cat_eye_color = (136, 170, 0)
black = (0, 0, 0)
cat = pygame.Surface((900, 1000))
cat.fill((128, 102, 0))
draw_ellipse_angle(cat, cat_color, [526, 140, 280, 100], -30, 0)
draw_ellipse_angle(cat, (0, 0, 0), [526, 140, 280, 100], -30, 1)
# hvost
ellipse(cat, cat_color, [96, 9, 524, 272], 0)
ellipse(cat, black, [96, 9, 524, 272], 1)
# telo
ellipse(cat, cat_color, [454, 132, 173, 166], 0)
ellipse(cat, black, [454, 132, 173, 166], 1)
ellipse(cat, cat_color, [591, 237, 57, 138], 0)
ellipse(cat, black, [591, 237, 57, 138], 1)
# zadnaya noga
ellipse(cat, cat_color, [126, 218, 129, 74], 0)
ellipse(cat, black, [126, 218, 129, 74], 1)
ellipse(cat, cat_color, [53, 100, 74, 129], 0)
ellipse(cat, black, [53, 100, 74, 129], 1)
# perednie nogy
ellipse(cat, cat_color, [19, 19, 218, 195], 0)
ellipse(cat, black, [19, 19, 218, 195], 1)
# liso
ellipse(cat, cat_eye_color, [57, 105, 56, 61], 0)
ellipse(cat, black, [57, 105, 56, 61], 1)
ellipse(cat, cat_eye_color, [149, 105, 56, 61], 0)
ellipse(cat, black, [149, 105, 56, 61], 1)
ellipse(cat, black, [88, 109, 8, 54], 0)
ellipse(cat, black, [180, 109, 8, 54], 0)
draw_ellipse_angle(cat, (255, 255, 255), [63, 124, 31, 10], -45, 0)
draw_ellipse_angle(cat, (255, 255, 255), [155, 124, 31, 10], -45, 0)
# glasa
polygon(cat, (255, 204, 170), [(119, 171), (138, 171), (130, 180)])
polygon(cat, black, [(119, 171), (138, 171), (130, 180)], 1)
line(cat, black, (130, 180), (130, 197))
pi = 3.14
arc(cat, black, (130, 194, 10, 10), pi, 2 * pi)
arc(cat, black, (120, 194, 10, 10), pi, 2 * pi)
# nos
polygon(cat, cat_color, [(14, 25), (70, 52), (29, 95)])
polygon(cat, black, [(14, 25), (70, 52), (29, 95)], 1)
polygon(cat, (255, 204, 170), [(21, 32), (63, 51), (33, 85)])
polygon(cat, black, [(21, 32), (63, 51), (33, 85)], 1)
polygon(cat, cat_color, [(169, 49), (222, 17), (212, 90)])
polygon(cat, black, [(169, 49), (222, 17), (212, 90)], 1)
polygon(cat, (255, 204, 170), [(177, 50), (216, 26), (209, 78)])
polygon(cat, black, [(177, 50), (216, 26), (209, 78)], 1)
# yshi


def liniy(x):
    line(cat, black, x[0], x[1])


m = [(155, 186), (268, 178)]
liniy(m)
m = [(155, 191), (268, 188)]
liniy(m)
m = [(155, 196), (268, 198)]
liniy(m)
m = [(98, 189), (0, 178)]
liniy(m)
m = [(98, 194), (0, 188)]
liniy(m)
m = [(98, 199), (0, 198)]
liniy(m)
# ysi
# конец котфа
# начало мяча
grey = (153, 153, 153)
ball = pygame.Surface((490, 257))
ball.fill((1, 0, 0))
line(ball, grey, (310, 175), (62, 175), 3)
circle(ball, (153, 153, 153), (383, 119), 100)
circle(ball, black, (383, 119), 100, 1)
for i in range(1, 4):
    arc(ball, black, (322 - (i-1)*15, 48 + (i-1)*15, 137, 116), 0, pi/2)
for i in range(1, 4):
    arc(ball, black, (336 + (i-1)*15, 92 + (i-1)*15, 79, 78), pi/2, pi)
ball.set_colorkey((1, 0, 0))
# конец мяча
# начало окна
window = pygame.Surface((794, 423))
window.fill((85, 68, 0))
rect(window, (213, 255, 230), (433, 100, 255, 305))
rect(window, (135, 205, 222), (453, 120, 98, 84))
rect(window, (135, 205, 222), (571, 120, 98, 84))
rect(window, (135, 205, 222), (453, 217, 98, 164))
rect(window, (135, 205, 222), (571, 217, 98, 164))

# конец окна
screen.blit(cat, (0, 473))
screen.blit(ball, (0, 773))
screen.blit(window, (0, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

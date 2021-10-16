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
screen.fill((128, 102, 0))


def window_loboy(x):
    window = pygame.Surface((1000, 423))
    window.fill((85, 68, 0))
    rect(window, (213, 255, 230), (503, 100, 255, 305))
    rect(window, (135, 205, 222), (523, 120, 98, 84))
    rect(window, (135, 205, 222), (641, 120, 98, 84))
    rect(window, (135, 205, 222), (523, 217, 98, 164))
    rect(window, (135, 205, 222), (641, 217, 98, 164))
    if x[0] == 1:
        screen.blit(window, x[1])
    else:
        window.set_colorkey((85, 68, 0))
        screen.blit(window, x[1])


def cot_loboy(x):
    # начало кота
    cat_color = x[0]
    cat_eye_color = x[4]
    black = (0, 0, 0)
    cat = pygame.Surface((900, 900))
    fon_color = (128, 102, 0)
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
    # конец кота
    if x[2] == 'r':
        cat = pygame.transform.flip(cat, 1, 0)
    cat = pygame.transform.rotozoom(cat, 0, x[1])
    cat.set_colorkey((fon_color))
    screen.blit(cat, x[3])


def ball_loboy(x):
    grey = (153, 153, 153)
    black = (0, 0, 0)
    ball = pygame.Surface((490, 257))
    ball.fill((1, 0, 0))
    line(ball, grey, (310, 175), (62, 175), 3)
    circle(ball, grey, (383, 119), 100)
    circle(ball, black, (383, 119), 100, 1)
    pi = 3.14
    for i in range(1, 4):
        arc(ball, black, (322 - (i-1)*15, 48 + (i-1)*15, 137, 116), 0, pi/2)
    for i in range(1, 4):
        arc(ball, black, (336 + (i-1)*15, 92 + (i-1)*15, 79, 78), pi/2, pi)
    if x[1] == 'r':
        ball = pygame.transform.flip(ball, 1, 0)
    ball = pygame.transform.rotozoom(ball, 0.0, x[0])
    ball.set_colorkey((1, 0, 0))
    screen.blit(ball, x[2])


window_loboy([1, (0, 50)])
window_loboy([0, (-300, 50)])
window_loboy([0, (-600, 50)])
ball_loboy([0.3, 'l', (100, 500)])
ball_loboy([0.3, 'l', (50, 800)])
ball_loboy([0.9, 'l', (-50, 770)])
ball_loboy([0.3, 'l', (450, 900)])
ball_loboy([0.5, 'r', (650, 800)])
ball_loboy([0.5, 'r', (450, 700)])
ball_loboy([0.3, 'r', (600, 680)])
# расцветки котов
grey_color_cat = (108, 93, 83)
blue_eye_color = (42, 212, 255)
cat_color_orange = (200, 113, 55)
cat_eye_color_green = (136, 170, 0)
# конец цветов
cot_loboy([grey_color_cat, 0.15, 'r', (50, 900), blue_eye_color])
cot_loboy([grey_color_cat, 0.4, 'r', (30, 650), blue_eye_color])
cot_loboy([cat_color_orange, 0.15, 'r', (0, 500), cat_eye_color_green])
cot_loboy([cat_color_orange, 0.15, 'r', (600, 750), cat_eye_color_green])
cot_loboy([cat_color_orange, 0.5, 'l', (400, 500), cat_eye_color_green])
cot_loboy([cat_color_orange, 0.15, 'l', (400, 850), cat_eye_color_green])
cot_loboy([grey_color_cat, 0.15, 'l', (650, 920), blue_eye_color])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

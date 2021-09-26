from random import randint
import turtle
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
for i in range(4):
    turtle.forward(600)
    turtle.left(90)
turtle.hideturtle()
x = [-1000]
y = [-1000]
number_of_turtles = 50
steps_of_time_number = 100
pool = []
for i in range(0, number_of_turtles):
    pool.append(turtle.Turtle(shape='circle'))
    pool[i].shapesize(0.5, 0.5, 0.5)
    pool[i].penup()
    pool[i].speed(50)
    a = randint(-300, 300)
    b = randint(-300, 300)
    a1 = []
    b1 = []
    for j in range(-5, 5, 1):
        a1.append(a+j)
        b1.append(b+j)
    while len(list(filter(lambda m: m in x, a1))) != 0 or len(list(filter(lambda m: m in y, b1))) != 0:
        a = randint(-300, 300)
        b = randint(-300, 300)
        a1 = []
        b1 = []
        for j in range(-5, 5, 1):
            a1.append(a+j)
            b1.append(b+j)
    x.append(a)
    y.append(b)
    pool[i].goto(a, b)
del x[0]
del y[0]
for i in range(steps_of_time_number):
    for unit in pool:
        a = randint(-5, 5)
        b = randint(-5, 5)
        r = pool.index(unit)
        a1 = []
        b1 = []
        for j in range(-1, 1, 1):
            a1.append(x[r]+a+j)
            b1.append(y[r]+b+j)
        while (len(list(filter(lambda n: n in x, a1))) != 0) and (len(list(filter(lambda n: n in y, b1))) != 0):
            a = randint(-5, 5)
            b = randint(-5, 5)
            a1 = []
            b1 = []
            for j in range(-1, 1, 1):
                a1.append(x[r] + a + j)
                b1.append(y[r] + b + j)
        if abs(x[r] + a) > 300:
            a = -a
        if abs(y[r] + b) > 300:
            b = -b
        unit.goto(x[r] + a, y[r] + b)
        x[r] += a
        y[r] += b

import turtle
turtle.shape('turtle')


def f(n):
    for i in range(n):
        k = (180 * (1 - ((n - 2) / n - (n - 3) * (1 - (n - 2) / 2 / n)))) % 180
        turtle.forward(100)
        turtle.left(k)


f(5)
turtle.penup()
turtle.forward(150)
turtle.pendown()
f(11)
x = input()

import turtle
turtle.shape('turtle')


def f(k):
    for i in range(180):
        turtle.forward(k)
        turtle.left(2)
    turtle.left(180)
    for i in range(180):
        turtle.forward(k)
        turtle.left(2)


turtle.left(90)
for i in range(1, 6, 1):
    f(i)
x = input(' ')

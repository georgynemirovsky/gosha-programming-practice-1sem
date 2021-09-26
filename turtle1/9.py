import turtle
turtle.shape('turtle')


def f(k):
    for i in range(180):
        turtle.forward(3)
        turtle.left(2)
    turtle.left(180)
    for i in range(180):
        turtle.forward(3)
        turtle.left(2)


for i in range(3):
    f(i)
    turtle.left(60)
x = input(' ')

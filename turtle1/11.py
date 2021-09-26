import turtle
turtle.shape('turtle')
turtle.left(90)


def f(k):
    for i in range(90):
        turtle.forward(0.5)
        turtle.right(2)
    for i in range(90):
        turtle.forward(0.1)
        turtle.right(2)


for i in range(10):
    f(i)
x = input(' ')

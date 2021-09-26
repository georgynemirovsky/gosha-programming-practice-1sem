import turtle
turtle.shape('turtle')


def f(k):
    for i in range(180):
        turtle.forward(k)
        turtle.left(2)


turtle.color('black')
turtle.begin_fill()
f(3)
turtle.end_fill()
turtle.penup()
turtle.goto(-23, 43+85)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
f(0.5)
turtle.end_fill()
turtle.penup()
turtle.goto(23, 43+85)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
f(0.5)
turtle.end_fill()
turtle.penup()
turtle.goto(-43, 85)
turtle.pendown()
turtle.right(90)
turtle.width(8)
for i in range(90):
    turtle.forward(1.5)
    turtle.left(2)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.color('white')
turtle.begin_fill()
turtle.backward(20)
turtle.end_fill()
x = input()

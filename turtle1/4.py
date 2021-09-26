import turtle
turtle.shape('turtle')
m = 5
n = 5
for i in range(10, 101, 10):
    turtle.penup()
    turtle.goto(m-5, n-5)
    turtle.pendown()
    m -= 5
    n -= 5
    for j in range(0, 4, 1):
        turtle.forward(i)
        turtle.left(90)
x = input()

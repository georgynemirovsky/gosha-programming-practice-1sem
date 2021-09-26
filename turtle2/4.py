import turtle
turtle.shape('circle')
turtle.forward(1000)
turtle.backward(1000)
Vx = int(input())
Vy = int(input())
ay = -10
x, y = 0, 0
dt = 0
n = 0
k = Vx * 2 * (Vy / abs(ay))
for i in range(0, 12000):
    dt += 2 * (abs(Vy) / abs(ay)) / 100000
    if y < 0:
        y = 0
        Vy = abs(Vy) / 1.4
    else:
        y += Vy*dt
        Vy += ay * dt
        x += Vx * dt
    turtle.goto(x, y)

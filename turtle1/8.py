import turtle as t
t.shape('turtle')


def f(n):
    for i in range(n):
        t.forward(50 + (n - 2) * 10)
        t.left(180 - (180 * (n - 2) / n))


m = 0
n = -300
for i in range(3, 13, 1):
    t.penup()
    t.goto(m - 5, n - 5)
    t.pendown()
    m -= 5
    n -= 5
    f(i)
x = input()
# сказали, что подойдёт

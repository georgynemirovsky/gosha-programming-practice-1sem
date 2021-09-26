import turtle as t
with open(r'C:\Users\Копатыч2\Desktop\лабы инфа\turtle2\shrift.txt', 'r') as f:
    d = f.readlines()
a = []
q = int(d[-1])
del d[-1]
for i in range(len(d)):
    a.append(list(map(int, d[i].split(' '))))
p = []
for i in range(len(a)):
    p.append([])
for i in range(len(a)):
    for j in range(0, len(a[i]), 2):
        p[i].append((a[i][j], a[i][j+1]))


def f(n):
    x = len(n)
    for j in range(x):
        for i in range(len(p[int(n[j])])):
            dx = p[int(n[j])][i][0]
            dy = p[int(n[j])][i][1]
            t.goto(dx + (j)*q, dy)
        t.penup()
        t.goto((j+1)*q, 0)
        t.pendown()


x = input()
f(x)

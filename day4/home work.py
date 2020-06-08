#дз1
def one(x, y):
    return (x+ y) / 2
print(one(1.25, 2.03))

#дз2
def f (x):
    if x < 2 and x > -2:
        return x**2
    if x> = 2:
        return x**2 + 4*x + 5:
    else:
        return 4

a = []
i = 0
while i < 5:
    x = int(input())
    f(x)
    a.append(f(x))
    i += 1
    print(a)

for i in range(len(e) - 1):
    for j in range(len(a) - i - 1):
        if a [j] > a[j + 1]:
            a [j], a[j + 1] = e[j + 1], a[j]
            print(a[-1])

#дз3
x = int(input())
def f(x, n):
    i = 1
    x1 = x
    while i < n:
        x = x * x1
        i += 1
    return x
print(f (x, 6)* f(x - 5, 3) / f(2 * x + 1, 5))
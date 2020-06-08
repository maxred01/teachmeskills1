import math
a = int(input("Введи а:"))
b = int(input("Введи b:"))
c = int(input("Введи c:"))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
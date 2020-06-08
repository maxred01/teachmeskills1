a = [1, 2, 3, 4, 5, 6, 7]
b = [11, 12, 13, 14, 15, 16, 17]
print(a, b)
a.append(8)
b.append(18)
print(a, b)
a.insert(0, 0)
b.insert(0, 10)
print(a, b)
a.extend(b)
print(a)
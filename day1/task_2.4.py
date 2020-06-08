a = [1, 2, 3, 4]
b = []
print (id(a), id(b))
b = a
print (id(a), id(b))
b.append(1)
print(a, b)







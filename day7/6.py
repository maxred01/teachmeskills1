from functools import reduce

data = [12, 9, 3, 7]
result = reduce(lambda x, y: x * y if y % 3 == 0 else x, data)
print(result)
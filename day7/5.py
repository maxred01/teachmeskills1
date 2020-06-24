data = ['Katia', 'pasha', 'masha','timur']
result = list(filter(lambda x: 'K' in x or 'k' in x, data))
print(result)
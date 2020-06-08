a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
max_element = 0

for i in a:
    for j in range (len(i)):
        if j == 1 and max_element  <i[j]:
            max_element = i[j]
print(max_element)

def max_element_in_matrix(matrix, position):
    if len(matrix[0])>= position -1:
        max_element = 0
    for i in matrix:
        for j in range(len(i)):
            if j == 1 and max_element < i[j]:
                max_element = i[j]
        return max_element
    return 'error'
print(max_element_in_matrix(a, 1))


def max_element_in_matrix(matrix, element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] = element:
            if matrix[i][j] = 0
    return matrix

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(change_element_by_value(a,8))
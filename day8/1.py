#1
my_fail = open('test.txt')
print(my_fail.readline())

#2
with open("test.txt", "r") as file:
    contents = file.readlines()
    str = contents[4]
    print(str)

#3
    str1 = contents[0:5]
    print(''.join(str1))
#4
    str1 = contents[0:2]
    print(''.join(str1))
#5
my_fail = open('test.txt')
print(my_fail.read())

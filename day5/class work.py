#1
#import random

def generage_matrix(n):
    data = []
    for i in range(0, n):
        stroka = []
          stroka.append(random.randrange(0, 100))
        data.append(stroka)
    print(data)

n = int(input())
generage_matrix(n)

#2
import random

def generage_matrix(n):
    data = []
    sum_matrix = 0
    tree[]
    for i in range(0, n):
        stroka = []
        for j in range(0, n):
            namber = random.randrange (1, 100)
            stroka.append(namber)
            if namber % 3 = 0:
               tree. append(namber)
               sum_matrix += namber
        data.append(stroka)
    print(data)
    print(tree)
    print(sum_matrix)

n = int(input())
generage_matrix(n)

#3
import random

def generage_matrix(n, m):
    data = []
    counter = 0
    for i in range(0, n):
        stroka = []
        for j in range(0, m):
            namber = random.randrange (1, 100)
            stroka.append(namber)
            if namber == 7:
                counter +=1
        data.append(stroka)
    print(data)
    print(counter)

n = int(input())
m = int(input())

generage_matrix(n, m)

#4
import random

def generage_matrix(n, m):
    data = []
    average = 0
    for i in range(0, n):
        stroka = []
        for j in range(0, m):
            namber = random.randrange (1, 100)
            average += namber
            stroka.append(namber)
        data.append(stroka)
    namber = namber / (n * m)

    for i in range(0, n):
        for j in range(0, m):
               counter += 1
    print(counter)

n = 4
m = 5
generage_matrix(n, m)

#7
n = int(input('От: '))
m = int(input('До: '))
counter = int(input(' Количество попыток: '))

namber = random.randrange(1, 100)
used = 0
correct = False

for i in range(counter):
   user_number = int(input())

   if user_number <= n and user_number >= m:
       print(f'number is not range {n}- {m}')
    if user_number == namber:
        correct = True
        print('You are the winner')
        break
if correct is False:
    print('You are the loser')

#1
string = 'hello world hello minsk hello sant-piterburg'
words = {}
longs_word = ''
counter_word =string.split()[0]

for i in string.split():
    if len(longs_word) < len(i):
        longs_word = i

    if i in words:
        words[i] += 1
    else:
        words[i] = 1

    if counter_word not in words:
        counter_word = i

print(words)
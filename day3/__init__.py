#string = 'hellow world'.split()[::-1]
#print(string)
#new_string = ' '.join(string)
#print(new_string)
#print(f"! {new_string} !")

#string = input()
#if len(string)%3==0:
#    print(f"{string}!")

#string = 'code hellow test'.split()[::-1]
#if 'code' in string:
#    print(True)
#else:
#    print(False)


#age = input('age: ')
#if int()

#string = input()
#if int(string)>5:
#    print(True)


import math

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")



#many = input().split()[::-1]
#if many(.) in print('рубля')


#string = "guufuyu@gmail.com".split("@")
#if 'gmail.com' == string[1]:
#    print('@'.join(string))
#else:
#    print("домен не найден")


tsx_list = ['TBX', 'TAX', 'TEX']
tax_other = ['TBX', 'TAX']
string = '7 TBX 0100'
list_number = string.split()
try:
    if len(string) ==10:
        if int(list_number[0]) >= 1 and int(list_number[0]) <=7:
            if int(list_number[0]) ==7 and list_number[1] in tsx_list:
                if len(list_number[2]) ==4 and list_number[2].isdigit() and int(list_number[2])>2:
                    print('correct')
            elif int(list_number[0]) == 7 and list_number[1] in tsx_list:
                if len(list_number[2]) == 4 and list_number[2].isdigit() and int(list_number[2]) > 0:
                    print('correct')
except:
    print('Value error')




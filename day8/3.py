my_fail = open('test1.txt', 'a')
my_fail.writelines('%s\n'%input() for i in range(1))
my_fail.close()
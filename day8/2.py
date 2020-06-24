my_fail = open('test1.txt', 'w')
my_fail.writelines('%s\n'%input() for i in range(6))
my_fail.close()



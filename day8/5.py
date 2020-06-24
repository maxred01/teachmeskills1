q = 0
with open('test1.txt', 'r+') as a:
    with open('test.txt', "w+") as b:
        with open('test2.txt', "w+") as c:
            for line in a:
                q+=1
                if q%2==0:
                    b.write(line)
                else:
                    c.write(line)
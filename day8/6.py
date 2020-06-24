with open('test.txt', 'r+') as a:
    with open('test1.txt', "r+") as b:
        q = a.readlines()
        s = b.readlines()
        l = 0
        for i in q:
           l+=1
           if i in s:
                    continue
           else:
                print(l,i)
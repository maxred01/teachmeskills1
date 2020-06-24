with open('test.txt', 'r+') as d, open('test1.txt', "w+") as f:
    t = d.read()
    for line in t:
            if line == '0':
                f.write('1')
            elif line =='1':
                f.write('0')
            else:
                f.write(line)
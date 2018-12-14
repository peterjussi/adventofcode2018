with open('2a.txt') as f:
    input = f.readlines()

for k in range(1, 27):
    lineno = 0
    for i in input[:-1]:
        lineno += 1
        for j in input[lineno:]:
            if i[:k-1] + i[k:] == j[:k-1] + j[k:]:
                print('The matching letters are: ' + i[:k-1] + i[k:])
                quit()

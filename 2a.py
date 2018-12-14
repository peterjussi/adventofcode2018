with open('2a.txt') as f:
    input = f.readlines()

doubles = 0
triples = 0

for i in input:
    i.strip()
    dic = {}
    for c in i:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    if 2 in dic.values():
        doubles += 1
    if 3 in dic.values():
        triples += 1

print('Doubles: ' + str(doubles))
print('Triples: ' + str(triples))
print('Checksum: ' + str(doubles*triples))

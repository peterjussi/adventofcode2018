import re

with open('3b.txt') as f:
    input = f.readlines()

fabric = {}
claims = {}
pattern = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'

for i in input:
    id, x, y, w, h = [int(s) for s in re.search(pattern, i).group(1, 2, 3, 4, 5)]
    claims[id] = 1

    for j in range(w):
        for l in range(h):
            coord = str(x+j) + '_' + str(y+l)
            if coord in fabric:
                try:
                    del(claims[id])
                except KeyError:
                    pass

                try:
                    del(claims[fabric[coord]])
                except KeyError:
                    pass
            else:
                fabric[coord] = id

print(claims)

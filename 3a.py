import re

with open('3a.txt') as f:
    input = f.readlines()

fabric = {}
overlap = 0
pattern = '#\d+ @ (\d+),(\d+): (\d+)x(\d+)'

for i in input:
    x, y, w, h = [int(s) for s in re.search(pattern, i).group(1, 2, 3, 4)]

    for j in range(w):
        for l in range(h):
            coord = str(x+j) + '_' + str(y+l)
            if coord in fabric:
                fabric[coord] += 1
                if fabric[coord] == 2:
                    overlap += 1
            else:
                fabric[coord] = 1

print(overlap)

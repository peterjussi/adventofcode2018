with open('1a.txt') as f:
    input = f.readlines()

shift = 0
for i in input:
    i.strip()
    shift += int(i)
print(shift)

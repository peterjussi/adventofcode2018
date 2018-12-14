with open('1b.txt') as f:
    input = f.readlines()

shift = 0
history = {}
found = False

while not found:
    for i in input:
        i.strip()
        shift += int(i)
        if shift not in history:
            history[shift] = 0;
        else:
            print('Shift in history. The answer is ' + str(shift) + '.')
            found = True
            break

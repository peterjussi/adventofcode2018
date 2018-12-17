import re
import operator

with open('4a.txt') as f:
    input = sorted(f.readlines())

eventpattern = '\[([\d\-]+)\s(\d+)\:(\d+)\]\s(\w+)'
guardpattern = '#(\d+)'
workchart = {}
sleepchart = {}
sleepcount = {}
endtime = 59

for i in input:
    date, hour, minute, event = re.search(eventpattern, i).group(1, 2, 3, 4)
    print(date, hour, minute, event)

    if event == 'Guard':
        guard = re.search(guardpattern, i).group(1)
        waketime = 0
    elif event == 'falls':
        sleeptime = int(minute)

        if date not in sleepchart:
            sleepchart[date] = {}

        if guard not in workchart:
            workchart[guard] = []

        if date not in workchart[guard]:
            workchart[guard].append(date)
    else:
        waketime = int(minute)

        for k in range(sleeptime, waketime):
            if guard in sleepcount:
                sleepcount[guard] += 1
                sleepchart[date][k] = 1
            else:
                sleepcount[guard] = 1
                sleepchart[date][k] = 1

sleepiestguard = max(sleepcount.items(), key=operator.itemgetter(1))[0]
print(sleepiestguard, sleepcount[sleepiestguard])

sleepychart = {}

for workday in workchart[sleepiestguard]:
    for k in range(0, 60):
        if k in sleepchart[workday]:
            if k in sleepychart:
                sleepychart[k] += 1
            else:
                sleepychart[k] = 1

sleepiestminute = max(sleepychart.items(), key=operator.itemgetter(1))[0]
print(sleepiestminute)
print(int(sleepiestguard)*int(sleepiestminute))
print(sleepychart)

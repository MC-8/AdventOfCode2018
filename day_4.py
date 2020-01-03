from collections import deque
from datetime import datetime
from time import perf_counter, sleep
def compare(S1, S2):
    yyyy1, mo1, dd1, hh1, mm1 = [int(x) for x in S1.split() if x.isdigit()]
    yyyy2, mo2, dd2, hh2, mm2 = [int(x) for x in S2.split() if x.isdigit()]
    t1 = datetime(yyyy1,mo1,dd1,hh1,mm1)
    t2 = datetime(yyyy2,mo2,dd2,hh2,mm2)
    return (t1-t2).seconds

L = []
Q = deque()
for s in open('4.in', 'r').readlines():
    L.append(s)
    Q.append(s)

t1 = perf_counter()
LS = sorted(L, key=lambda x: datetime.strptime(x[x.index('[')+1:x.index(']')], '%Y-%m-%d %H:%M'))
t2 = perf_counter()
print(f"Sorted list in {t2-t1:2.3f}s")

il = 0
l = LS[il]
D = {}
while il < len(LS)-1:
    if "Guard" in (l:=LS[il]):
        # begin shift, extract ID
        ID = l[l.index('#')+1:].split()[0]
        begin_time = None
        end_time = None
        if ID not in D:
            D[ID] = []
        il+=1
        while "Guard" not in LS[il]:
            if "falls" in (l:=LS[il]):
                mm1 = l[l.index(':')+1:].split(']')[0]
                begin_time = int(mm1)
            if "wakes" in LS[il]:
                mm1 = l[l.index(':')+1:].split(']')[0]
                end_time = int(mm1)
            if begin_time and end_time:
                D[ID].append(range(begin_time, end_time))
                begin_time = None
                end_time = None
            il+=1
            if il>len(LS)-1: break
    else:
        il+=1

tot_min_best = 0
min_best = 0
ID_best = 0
max_sleeping_time = 0
# Find guard which sleeps the most
for d in D:
    sleeping_time = 0
    for x in D[d]:
        sleeping_time += len(x)
    print(f"{d} slept {sleeping_time}")
    if sleeping_time > max_sleeping_time:
        # candidate sleepy guard:
        ID_best = int(d)
        max_sleeping_time = sleeping_time

tot_min_best = 0
for minute in range(60):
    if (mins:=sum([x.count(minute) for x in D[str(ID_best)]])) > tot_min_best:
        tot_min_best = mins
        min_best = minute

print(f"Solution part 1 = {ID_best*min_best}") # 51232 too low, 100000 too low

with open('your_file.txt', 'w') as f:
    for item in LS:
        f.write("%s" % item)

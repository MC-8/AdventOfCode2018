from collections import deque
from datetime import datetime
from time import perf_counter

LS = []
for s in open('4.in', 'r').readlines():
    LS.append(s)

t1 = perf_counter()
LS = sorted(LS, key=lambda x: datetime.strptime(x[x.index('[')+1:x.index(']')], '%Y-%m-%d %H:%M'))
t2 = perf_counter()
print(f"Sorted list in {t2-t1:2.3f}s")

il = 0
l = LS[il]
D = {}
while il < len(LS):
    if "Guard" in (l:=LS[il]):
        # begin shift, extract ID
        ID = int(l[l.index('#')+1:].split()[0])
        begin_time = None
        end_time = None
        if ID not in D:
            D[ID] = []
            #D[ID] = 0
        il+=1
        while "Guard" not in LS[il]:
            if "falls" in (l:=LS[il]):
                mm1 = l[l.index(':')+1:].split(']')[0]
                begin_time = int(mm1)
            if "wakes" in (l:=LS[il]):
                mm1 = l[l.index(':')+1:].split(']')[0]
                end_time = int(mm1)
            if begin_time is not None and end_time is not None:
                D[ID].append(range(begin_time, end_time))
                # D[ID] += 1
                begin_time = end_time = None
            il+=1
            if il>len(LS)-1: break


tot_min_best = 0
min_best = 0
ID_best = 0
max_sleeping_time = 0
# Find guard which sleeps the most
for d in D:
    sleeping_time = 0
    for x in D[d]:
        sleeping_time += len(x)
    if sleeping_time > max_sleeping_time:
        # candidate sleepy guard:
        ID_best = d
        max_sleeping_time = sleeping_time

tot_min_best = 0
for minute in range(60):
    if (mins:=sum([x.count(minute) for x in D[ID_best]])) > tot_min_best:
        tot_min_best = mins
        min_best = minute

print(f"Solution part 1 = {ID_best*min_best}") 

d_best = 0
overall_best = 0
minute_best = 0
for d in D:
    sleeping_time = 0
    tot_min_best = 0
    min_best = 0
    for minute in range(60):
        if (mins:=sum([x.count(minute) for x in D[d]])) > tot_min_best:
            tot_min_best = mins
            min_best = minute
    if tot_min_best > overall_best:
        # candidate sleepy guard:
        overall_best = tot_min_best
        minute_best = min_best
        d_best = d
print(f"Solution part 2 = {d_best*minute_best}") # 85509 too high

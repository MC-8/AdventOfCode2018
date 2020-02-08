from itertools import product
from collections import deque, namedtuple

LS = set()
for s in open('6.in', 'r').readlines():
    LS.add(tuple(int(x) for x in s.strip().split(',')))

def getManhattanDistance(p1:tuple, p2:tuple) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

D_closest_to = {}
to_remove = set()
for x,y in product(range(-220, 550), range(-220, 550)):
    for s in LS:
        if D_closest_to.get((x,y),(None, 1e6))[1] == getManhattanDistance((x,y), s):
            to_remove.add((x,y))
        elif D_closest_to.get((x,y),(None, 1e6))[1] > getManhattanDistance((x,y), s):
            D_closest_to[(x,y)] = (s, getManhattanDistance((x,y), s))

# print(D_closest_to)
Dunique = {}
for k in D_closest_to:
    v = D_closest_to[k]
    if k not in to_remove:
        Dunique[v[0]] = Dunique.get(v[0],0)+1

print(Dunique)
# # State = namedtuple('State', 'point source distance')

# # Q = deque()
# # Dvisited = {} 
# # Dunique = {}
# # def up(p): return (p[0],p[1]-1)
# # def down(p): return (p[0],p[1]+1)
# # def left(p): return (p[0]-1,p[1])
# # def right(p): return (p[0]+1,p[1])

# # for s in LS:
# #     Q.append(State(up(s),   s, 1))
# #     Q.append(State(down(s), s, 1))
# #     Q.append(State(left(s), s, 1))
# #     Q.append(State(right(s),s, 1))

# # while Q:
# #     state = Q.popleft()
# #     sp = state.point
# #     if (sp, state.source) in Dvisited: continue
# #     if (sp, state.source) not in Dvisited and sp not in LS and state.distance < 210:
# #         Dvisited[(sp, state.source)] = state.distance
# #         Dunique[sp] = (state.source, state.distance)
# #     elif sp in Dunique and state.distance < Dunique[sp][1]:
# #         Dvisited[(sp, state.source)] = state.distance
# #         Dunique[sp] = (state.source, state.distance)
# #     elif sp in Dunique and state.distance == Dunique[sp][1] and Dunique[sp][0] != state.source:
# #         try:
# #             del Dunique[sp]
# #         except KeyError:
# #             pass
# #     else:
# #         continue
# #     Q.append(State(up(sp),   state.source, state.distance + 1))
# #     Q.append(State(down(sp), state.source, state.distance + 1))
# #     Q.append(State(left(sp), state.source, state.distance + 1))
# #     Q.append(State(right(sp),state.source, state.distance + 1))
# # Dcount = {}

# # #print(Dunique)
# # for el in Dunique:
# #     Dcount[Dunique[el][0]] = Dcount.get(Dunique[el][0],0)+1
# # print(Dcount)
        




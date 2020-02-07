import re
from collections import defaultdict
class TreeNode(object):

    def __init__(self, value, parents = []) -> None:
        self.val = value
        self.parents = parents
        self.children = []

    def append_child(self, child) -> None:
        self.children.append(child)
    
    def append_parent(self, parent) -> None:
        self.parents.append(parent)


pairs = []
P2C = defaultdict(list)
C2P = defaultdict(int)
for l in open('7.in2','r').readlines():
    pair = (re.search(r'Step (.) must be finished before step (.)', l).group(1),
            re.search(r'Step (.) must be finished before step (.)', l).group(2))
    #print(pair)
    P2C[pair[0]].append(pair[1])
    C2P[pair[1]] += 1
    pairs.append(pair)

Q = []
for k in P2C:
    if C2P[k] == 0:
        Q.append(k)

print(Q)

sol = ''

while Q:
    x = sorted(Q)[0]
    sol += x
    Q.remove(x)
    for y in P2C[x]:
        C2P[y] -= 1
        if C2P[y]==0:
            Q.append(y)

print(sol)



# print(P2C)
# print(C2P)
parent_set = set()
child_set = set()
all_set = parent_set

for p,c in pairs:
        parent_set.add(p)
        child_set.add(c)
        all_set.add(p)
        all_set.add(c)

# print(parent_set)
# print(child_set)
# print(parent_set-child_set)

roots = [x for x in (parent_set-child_set)]
sol_order = sorted(roots)[0]
roots.remove(sorted(roots)[0])

owned = set(sol_order)
while True:
    reachables = set(roots)
    for s in owned:
        if s in P2C:
            for c in P2C[s]:
                reachables.add(c)
    possible = reachables - owned
    candidates = set()
    for r in possible:
        if r in C2P:
            pr = set()
            for p in C2P[r]:
                pr.add(p)
            if owned.issuperset(pr):
                candidates.add(r)
    if not(candidates) and set(roots).issubset(owned):
        print(f"{sol_order=}")
        break
    if not(candidates):
        next_step = sorted(roots)[0]
        roots.remove(sorted(roots)[0])
    else:
        next_step = sorted(candidates)[0]
    sol_order += next_step # BFUXCEGHIJKLDMNOPAQRSTVWYZ Not ok, BFUXELNGIRHQPSJKVTYOCZDWMA not OK. BFLNGIRUSJXEHKQPVTYOCZDWMA is OK
    owned.add(next_step)

    

# Part 2

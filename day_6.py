from collections import deque, namedtuple
from itertools import product
grid = []
for l in open('6.in','r').readlines():
    grid.append(l.strip())
    # Use example but the input will be different
xlim, ylim = len(grid), len(grid[0])    
print(grid)

state = namedtuple('state', 'origin coord dist')

Q = deque()
allstate = {}
have_been = set()

# Add initial states
for x,y in product(range(xlim), range(ylim)):
    if (origin:=grid[x][y]) in ['A','B','C','D','E','F']:
        s = state(origin = origin, coord= (x,y), dist=0)
        Q.append(s)
        allstate[(x,y)] = (origin, 0)
        have_been.add((origin,x,y))

counter = 0
while Q:
    s = Q.popleft()
    x,y = s.coord
    counter += 1
    if counter%10000 == 0:
        print(len(Q))
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        if xlim>(new_x:=x+dx)>=0 and ylim>(new_y:=y+dy)>=0 and ((s.origin,new_x,new_y) not in have_been):

            olds = allstate.get((new_x,new_y), ((-1,-1), float('inf')))
            
            if (new_dist := s.dist+1) < olds[1]:
                allstate[(new_x,new_y)] = (s.origin, new_dist)
                #grid[new_x][new_y] = s.origin
            elif (new_dist := s.dist+1) == olds[1] and s.origin != olds[0]:
                allstate[(new_x,new_y)] = ('x', new_dist)
                #grid[new_x][new_y] = 'x'
            have_been.add((s.origin,new_x,new_y))
            Q.append(state(origin=s.origin, coord=(new_x,new_y),dist=s.dist+1))

d_counter = 0
e_counter = 0
for x in allstate:
    if allstate[x][0] == 'D': d_counter +=1
    if allstate[x][0] == 'E': e_counter +=1

print(f"{d_counter=}")
print(f"{e_counter=}")


xmin, ymin = -1, -1
xmax, ymax = 400, 400

#     # Use example but the input will be different
# xlim, ylim = len(grid), len(grid[0])    
# print(grid)

state = namedtuple('state', 'origin coord dist')

Q = deque()
allstate = {}
have_been = set()


# Add initial states
for l in open('6.in2','r').readlines():
    origin = tuple([int(x) for x in l.split(',')])
    s = state(origin = origin, coord= origin, dist=0)
    Q.append(s)
    allstate[origin] = (origin, 0)
    have_been.add((origin,origin[0],origin[1]))

counter = 0
while Q:
    s = Q.popleft()
    x,y = s.coord
    counter += 1
    if counter%10000 == 0:
        print(len(Q))
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        if xmax>(new_x:=x+dx)>=xmin and ymax>(new_y:=y+dy)>=ymin and ((s.origin,new_x,new_y) not in have_been):

            olds = allstate.get((new_x,new_y), ((-1,-1), float('inf')))
            
            if (new_dist := s.dist+1) < olds[1]:
                allstate[(new_x,new_y)] = (s.origin, new_dist)
                #grid[new_x][new_y] = s.origin
            elif (new_dist := s.dist+1) == olds[1] and s.origin != olds[0]:
                allstate[(new_x,new_y)] = ('x', new_dist)
                #grid[new_x][new_y] = 'x'
            have_been.add((s.origin,new_x,new_y))
            Q.append(state(origin=s.origin, coord=(new_x,new_y),dist=s.dist+1))

d_counter = 0
e_counter = 0
area_counter = {}
for x in allstate:
    area_counter[allstate[x][0]] = area_counter.get(allstate[x][0],0) + 1

for k in area_counter:
    print(f"{k=},{area_counter[k]=}")


print("---------------")
# Remove keys that are in the borders (means their area is infinite)
for x in range(xmin, xmax+1):
    try:
        area_counter.pop(allstate[(x,0)][0])
    except KeyError:
        pass
    try:
        area_counter.pop(allstate[(x,ymax-1)][0])
    except KeyError:
        pass


for y in range(ymin, ymax+1):
    try:
        area_counter.pop(allstate[(0,y)][0])
    except KeyError:
        pass
    try:
        area_counter.pop(allstate[(xmax-1,y)][0])
    except KeyError:
        pass

for k in area_counter:
    print(f"{k=},{area_counter[k]=}")
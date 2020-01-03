D = {}
for S in open('3.in','r').readlines():
    S = S.replace(':',' ').replace('x',' ').replace('#',' ').replace('@', ' ').replace(',',' ').replace('\n',' ')
    ID, left_space, up_space, width, height = [int(s) for s in S.split() if s.isdigit()]
    for x in range(left_space, left_space+width):
        for y in range(up_space, up_space+height):
            D[(x,y)] = D.get((x,y),0) + 1
sol = 0
for x in range(1000):
    for y in range(1000):
        if D.get((x,y),0)>1:
            sol+=1
print(f"Solution part 1 = {sol}")


allIDs = set()
copyID = set()
D = {}
for S in open('3.in','r').readlines():
    S = S.replace(':',' ').replace('x',' ').replace('#',' ').replace('@', ' ').replace(',',' ').replace('\n',' ')
    ID, left_space, up_space, width, height = [int(s) for s in S.split() if s.isdigit()]
    allIDs.add(ID)
    copyID.add(ID)
    for x in range(left_space, left_space+width):
        for y in range(up_space, up_space+height):
            if (x,y) in D:
                try:
                    copyID.remove(ID)
                except KeyError:
                    pass
                try:
                    copyID.remove(D[(x,y)])
                except KeyError:
                    pass
            else:
                D[(x,y)] = ID

print(f"Solution part 2 = {copyID}")
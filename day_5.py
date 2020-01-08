from copy import deepcopy
S = open('5.in','r').readline().strip()
change = True
while change:
    lenbefore = len(S)
    for r in [chr(ord('a')+x)+chr(ord('A')+x) for x in range(26)]:
        S = S.replace(r,'')
    for r in [chr(ord('A')+x)+chr(ord('a')+x) for x in range(26)]:
        S = S.replace(r,'')
    change = lenbefore!=len(S)
print(f"Solution part 1 = {len(S)}")


S = open('5.in','r').readline().strip()
shortest = len(S)
for x in range(26):
    change = True
    C = deepcopy(S)
    r = chr(ord('a')+x)
    C = C.replace(r,'')
    r = chr(ord('A')+x)
    C = C.replace(r,'')
    i = 0
    while i<2:
        lenbefore = len(C)
        for r in [chr(ord('a')+y)+chr(ord('A')+y) for y in range(26)]:
            C = C.replace(r,'')
        for r in [chr(ord('A')+y)+chr(ord('a')+y) for y in range(26)]:
            C = C.replace(r,'')
        if lenbefore==len(C):
            i+=1
    if len(C) < shortest:
        shortest = len(C)
print(f"Solution part 2 = {shortest}")
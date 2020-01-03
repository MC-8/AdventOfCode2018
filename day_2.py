twos = 0
threes = 0
for S in open('2.in','r').readlines():
    for c in S:
        if S.count(c)==2:
            twos+=1
            break
    for c in S:
        if S.count(c)==3:
            threes+=1
            break
print(f"Solution part 1 = {twos*threes}")

done = False
sol = ''
for S in open('2.in','r').readlines():
    for K in open('2.in','r').readlines():
        count = 0
        isol = 0
        for i in range(len(K.strip())):
            if ord(S[i])-ord(K[i]):
                count += 1
                isol = i
        if count==1:
            sol = S[:isol]+S[isol+1:]
            assert (sol == K[:isol]+K[isol+1:])
            done = True
            break
    if done:
        break
print(f"Solution part 2 = {sol}")

frequency = 0
for l in open('1.in').readlines():
    frequency+=int(l)
print(f"Solution part 1 = {frequency}")

frequency = 0
S = set()
done = False
while not done:
    for l in open('1.in').readlines():
        frequency+=int(l)
        if frequency in S:
            print(f"Solution part 2 = {frequency}")
            done = True
            break
        else:
            S.add(frequency)

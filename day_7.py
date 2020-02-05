import re
for l in open('7.in','r').readlines():
    pair = (re.search(r'Step (.) must be finished before step (.)', l).group(1),
            re.search(r'Step (.) must be finished before step (.)', l).group(2))
    print(pair)
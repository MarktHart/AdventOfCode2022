import re

qs, ls = open('i').read().split('\n\n')
qs = [[q[i] for i in range(1, len(q), 4)] for q in qs.split('\n')[-2::-1]]
qs = list(zip(*qs))
qs = [[a for a in b if a != ' '] for b in qs]

r = 0
for l in ls.split('\n')[:-1]:
    a,b,c = map(int, re.search(r'.*?(\d+)'*3, l).groups())
    for _ in range(a):
        if qs[b-1]:
            qs[c-1].append(qs[b-1].pop())

print(''.join(q[-1] for q in qs if q))

import itertools

s, k = input().split()
k = int(k)
all = []
for pair in list(itertools.permutations(s)):
    all.append("".join(pair))
all = list(set(all))
all.sort()
print(all[k-1])
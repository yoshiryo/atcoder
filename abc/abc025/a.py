import itertools
s = input()
all = list(itertools.product(s, repeat=2))
n = int(input())
print("".join(all[n-1]))
import itertools
n = int(input())
s = input()
all = list(itertools.permutations(s, n))
for t in all:
    t = "".join(t)
    if t != s and s != t[::-1]:
        print(t)
        exit()
print("None")
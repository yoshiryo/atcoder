import itertools
n = int(input())
p = list(map(int, input().split()))
np = int("".join(map(str, p)))
q = list(map(int, input().split()))
nq = int("".join(map(str, q)))
l = list(itertools.permutations(range(1, n+1)))
all = []
for a in l:
    all.append(int("".join(map(str, a))))
for i in range(len(all)):
    if all[i] == np:
        num_p = i+1
    if all[i] == nq:
        num_q = i+1
print(abs(num_p - num_q))
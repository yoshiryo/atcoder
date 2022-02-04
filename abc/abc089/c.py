import itertools
n = int(input())
cnt = [0]*5
for _ in range(n):
    s = input()
    if s[0] == "M":
        cnt[0] += 1
    elif s[0] == "A":
        cnt[1] += 1
    elif s[0] == "R":
        cnt[2] += 1
    elif s[0] == "C":
        cnt[3] += 1
    elif s[0] == "H":
        cnt[4] += 1

l = list(itertools.combinations(cnt, 3))
ans = 0
for i in l:
    ans += i[0]*i[1]*i[2]
print(ans)
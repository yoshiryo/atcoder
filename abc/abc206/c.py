from collections import Counter

n = int(input())
a = list(map(int, input().split()))
all = len(a)
c = Counter(a)
key = list(c.keys())
ans = 0
for i in range(len(key)):
    cnt = c[key[i]]
    ans += cnt*(all - cnt)
print(ans//2)

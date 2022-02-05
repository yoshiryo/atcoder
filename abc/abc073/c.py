from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]
c = Counter(a)
ans = 0
for _, val in c.items():
    if val%2 == 1:
        ans += 1
print(ans)
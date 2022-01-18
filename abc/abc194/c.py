from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = 0
for i in range(-200, 200):
    for j in range(i+1, 201):
        ans += cnt[i]*cnt[j]*(i-j)**2

print(ans)
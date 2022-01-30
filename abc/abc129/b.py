n = int(input())
w = list(map(int, input().split()))
all = sum(w)
now = 0
ans = all
for i in range(n):
    all -= w[i]
    now += w[i]
    ans = min(ans, abs(all - now))
print(ans)
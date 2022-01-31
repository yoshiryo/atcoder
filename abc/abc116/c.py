n = int(input())
h = list(map(int, input().split()))
ma = max(h)
ans = 0
for i in range(ma+1):
    cnt = 0
    judge = True
    for j in range(n):
        if h[j] > i:
            if judge:
                cnt += 1
                judge = False
        else:
            judge = True
    ans += cnt
print(ans)
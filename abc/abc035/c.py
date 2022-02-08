n, q = map(int, input().split())
cnt = [0]*(n+1)
for _ in range(q):
    l, r = map(int, input().split())
    cnt[l-1] += 1
    cnt[r] -= 1
su = 0
ans = []
for i in range(n):
    su += cnt[i]
    if su%2 == 0:
        ans.append("0")
    else:
        ans.append("1")
print("".join(ans))
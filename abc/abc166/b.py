n, k = map(int, input().split())
ans = [0]*n
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in range(d):
        ans[a[i] - 1] += 1
cnt = 0
for a in ans:
    if a == 0:
        cnt += 1
print(cnt)
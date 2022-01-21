n = int(input())
a = list(map(int, input().split()))
ans = []

for k in range(2, 1001):
    cnt = 0
    for i in range(n):
        if a[i]%k == 0:
            cnt += 1
    ans.append([cnt, k])
ans = sorted(ans, key=lambda x:x[0], reverse=True)
print(ans[0][1])

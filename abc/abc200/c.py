n = int(input())
a = list(map(int, input().split()))
l = [0]*200
for i in range(n):
    l[a[i]%200] += 1
ans = 0
for i in range(200):
    if l[i] >= 2:
        ans += (l[i]*(l[i] - 1))//2
print(ans)
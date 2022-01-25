k, n = map(int, input().split())
a = list(map(int, input().split()))
a = [(k - a[-1])*-1] + a
ans = []
for i in range(n):
    ans.append(a[i+1] - a[i])
print(k - max(ans))
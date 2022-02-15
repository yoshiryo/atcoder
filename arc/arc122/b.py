n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
x = a[n//2]/2
for i in range(n):
    ans += x + a[i] - min(a[i],2*x)
print(ans/n)
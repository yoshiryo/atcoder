n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = [10**9]*n
ans[0] = t[0]
for i in range(2*n):
    ans[(i+1)%n] = min(ans[i%n] + s[i%n], t[(i+1)%n])
for i in ans:
    print(i)
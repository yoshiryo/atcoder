n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
diff = 10**10
for i in range(n):
    T = t - h[i]*0.006
    if diff > abs(T - a):
        ans = i
        diff = abs(T - a)
print(ans+1)
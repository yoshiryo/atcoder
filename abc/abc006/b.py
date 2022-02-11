n = int(input())
mod = 10**4 + 7
a = [0, 0, 1]
for i in range(3, n):
    a.append(a[i-1]%mod + a[i-2]%mod + a[i-3]%mod)
print(a[n-1]%mod)
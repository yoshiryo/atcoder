n = input()
ans = 0
mod = 998244353
l = len(n)
n = int(n)
for i in range(l-1):
    now = 10**(i+1) - (10**i - 1) - 1
    ans += now*(now+1)//2
p = 10**(l-1) - 1
diff = n - p
ans += (diff)*(diff+1)//2
print(ans%mod)
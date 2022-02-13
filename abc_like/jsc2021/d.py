MOD = 10 ** 9 + 7
N, P = map(int, input().split())
x = P - 1
y = pow(P - 2, N - 1, MOD) 
ans = (x * y) % MOD
print(ans)
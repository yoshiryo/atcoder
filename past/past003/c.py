a, r, n = map(int, input().split())
n -= 1
for _ in range(n):
    a *= r
    if a > 10**9:
        print("large")
        exit()
print(a)
n = int(input())
p = [int(input()) for _ in range(n)]
ma = max(p)
ans = sum(p) - ma//2
print(ans)
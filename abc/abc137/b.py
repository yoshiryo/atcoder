k, x = map(int, input().split())
l = max(-1000000, x - k + 1)
r = min(1000000, x + k - 1)
ans = [i for i in range(l, r+1)]
print(*ans)
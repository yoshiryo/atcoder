a, b = map(int, input().split())
ans = max(a*2 - 1, b*2 - 1, a+b)
print(ans)
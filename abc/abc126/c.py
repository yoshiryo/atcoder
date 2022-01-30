n, k = map(int, input().split())
ans = 0
for i in range(1, n+1):
  s = i
  cnt = 0
  while s < k:
    cnt += 1
    s *= 2
  ans += 1/n * (1/2)**cnt
print(ans)
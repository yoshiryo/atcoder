n, l = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
ans = ""
for i in s:
    ans += i
print(ans)
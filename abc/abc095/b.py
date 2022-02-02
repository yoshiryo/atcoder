n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
m.sort()
mi = m[0]
su = sum(m)
x -= su
ans = n
print(ans + x//mi)
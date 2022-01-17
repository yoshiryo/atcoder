h, w, x, y = map(int, input().split())
s = [input() for i in range(h)]
x -= 1
y -= 1
ans = 1
p = x
while True:
    p -= 1
    if s[p][y] == "#" or p < 0:
        break
    else:
        ans += 1

p = x
while True:
    p += 1
    if p >= h or s[p][y] == "#":
        break
    else:
        ans += 1

p = y
while True:
    p -= 1
    if s[x][p] == "#" or p < 0:
        break
    else:
        ans += 1

p = y
while True:
    p += 1
    if p >= w or s[x][p] == "#":
        break
    else:
        ans += 1

print(ans)
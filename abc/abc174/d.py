n = int(input())
c = input()
r = c.count("R")
w = 0
cnt = 2090000
for i in range(n):
    if r < w:
        cnt = min(cnt, w)
    else:
        cnt = min(cnt, r)
    if c[i] == "W":
        w += 1
    else:
        r -= 1
cnt = min(cnt, c.count("W"))

print(cnt)

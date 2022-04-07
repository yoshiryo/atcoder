n = int(input())
t = input()
x, y = 0, 0
d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
cnt = 0
for i in range(n):
    if t[i] == "R":
        cnt += 1
    else:
        x += d[cnt%4][0]
        y += d[cnt%4][1]
print(x, y)

n = int(input())
c = [list(map(int, input().split())) for _ in range(n-1)]
now = 0
ans = []
for i in range(n-1):
    now = c[i][0] + c[i][1]
    for j in range(i+1, n-1):
        if now <= c[j][1]:
            now = c[j][1]
            now += c[j][0]
        else:
            a = now - c[j][1]
            b = a%c[j][2]
            if b != 0:
                now += c[j][2] - b
            now += c[j][0]
    ans.append(now)
ans.append(0)

for i in ans:
    print(i)
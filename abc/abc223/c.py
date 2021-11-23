n = int(input())
ab = []
sec = 0
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    sec += a/b
    ab.append([a, b])

sec /= 2

for i in range(n):
    if sec > ab[i][0]/ab[i][1]:
        ans += ab[i][0]
        sec -= ab[i][0]/ab[i][1]
    else:
        ans += sec*ab[i][1]
        break
print(ans)


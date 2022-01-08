h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
ans = 0
p = True
for i in range(h):
    if not p:
        break
    for j in range(w):
        if j == w - 1 and b[i][j] != a[i][j]:
            p = False
            break
        elif j == w - 1 and b[i][j] == a[i][j]:
            break
        elif i == h - 1 and b[i][j] != a[i][j]:
            p = False
            break
        elif i == h - 1 and b[i][j] == a[i][j]:
            break
        else:
             diff = b[i][j] - a[i][j]
             a[i][j] += diff
             a[i+1][j] += diff
             a[i][j+1] += diff
             a[i+1][j+1] += diff
             ans += abs(diff)
if p:
    print("Yes")
    print(ans)
else:
    print("No")
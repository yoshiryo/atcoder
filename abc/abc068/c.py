n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
x = []
for i in range(m):
    if ab[i][0] == 1:
        x.append(ab[i][1])
    elif ab[i][1] == n:
        x.append(ab[i][0])
l = len(x)
if l == len(set(x)):
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
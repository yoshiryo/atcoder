h, w = map(int, input().split())
A = []
mi = 101
ans = 0
for _ in range(h):
    a = list(map(int, input().split()))
    mi = min(mi, min(a))
    A.append(a)
for i in range(h):
    for j in range(w):
        if A[i][j] > mi:
            ans += A[i][j] - mi
print(ans)


n, x, y = map(int, input().split())
x -= 1
y -= 1
k = [0]*(n-1)
for i in range(n-1):
    for j in range(i+1, n):
        d = min(j-i, abs(x-i) + abs(y-j) + 1)
        k[d-1] += 1

for ans in k:
    print(ans)
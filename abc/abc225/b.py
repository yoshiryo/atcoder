n = int(input())
g = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b)
    g[b-1].append(a)
for i in range(n):
    if len(g[i]) == n-1:
        print("Yes")
        exit()
print("No")
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
for i in range(k**n):
    cnt = 0
    for j in range(n):
        cnt ^= t[j][i//k**j%k]
    if cnt == 0:
        print("Found")
        exit()
print("Nothing")
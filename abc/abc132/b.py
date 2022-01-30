n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n-2):
    p1 = p[i]
    p2 = p[i+1]
    p3 = p[i+2]
    np = [p1, p2, p3]
    np.sort()
    if np[1] == p2:
        ans += 1
print(ans)
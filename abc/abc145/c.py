from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
L = list(permutations(range(1, n+1)))
ans = 0
for l in L:
    dis = 0
    for k in range(n-1):
        i = l[k] - 1
        j = l[k+1] - 1
        d = (xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2
        dis += d**0.5
    ans += dis
print(ans/len(L))

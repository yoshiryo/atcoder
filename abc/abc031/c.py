N = int(input())
As = list(map(int, input().split()))
ans = -float("inf")

for i in range(N):
    aoki = [] 
    for j in range(N):
        if i == j: continue

        left, right = min(i,j), max(i,j)
        Ts = As[left: right+1]  
        aoki.append(sum(Ts[1::2])) 
    j = aoki.index(max(aoki))
    left, right = min(i, j), max(i, j)
    Ts = As[left: right+1]
    ans = max(ans, sum(Ts[0::2]))
print(ans)
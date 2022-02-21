H,W,K,V = map(int,input().split())
A = []
for _ in range(H):
    d = list(map(int,input().split()))
    A.append(d)
S = [[0 for _ in range(W+1)] for _ in range(H+1)]
for i in range(H):
    sum = 0
    for j in range(W):
        sum += A[i][j] 
        S[i+1][j+1] = sum + S[i][j+1]
ans = 0
for x1 in range(W):
    for x2 in range(x1+1,W+1):
        for y1 in range(H):
            for y2 in range(y1+1,H+1):
                area = (y2-y1)*(x2-x1)
                if S[y2][x2]-S[y2][x1]-S[y1][x2]+S[y1][x1] + area * K <= V:
                    ans = max(ans,area)
print(ans)
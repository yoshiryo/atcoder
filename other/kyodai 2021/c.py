N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = float('inf')

points = [(0,0)]
for i in range(N):
    points.append((A[i],-1))
    points.append((B[i],1))
points.sort()

dist = [(0,0)]
pos = 0
neg = 0
count = 0
for i in range(2*N):
    count += points[i][1]
    if count >= 0:
        pos += points[i+1][0]-points[i][0]
    else:
        neg += points[i+1][0]-points[i][0]
    dist.append((pos,neg))

ans = INF
for i in range(2*N+1):
    tmp = dist[i][0] + dist[i][1]*3 + (points[2*N][0]-points[i][0])*2
    ans = min(ans,tmp)
print(ans)

h,w=map(int,input().split())
c=[]
for i in range(h):
  c.append(list(input()))
dp=[[float("inf")]*(w+1) for i in range(h+1)]
dp[0][0]=0
for i in range(h):
  for j in range(w):
    if c[i][j]=="E":
      dp[i][j+1]=min(dp[i][j+1],dp[i][j])
      dp[i+1][j]=dp[i][j]+1
    else:
      dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)
      dp[i+1][j]=dp[i][j]
print(dp[h-1][w])
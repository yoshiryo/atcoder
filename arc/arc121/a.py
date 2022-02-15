n = int(input())
X = []
Y = []
for _ in range(n):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
X_max = max(X)
X_min = min(X)
Y_max = max(Y)
Y_min = min(Y)
ans = []
for i in range(n):
    ans.append(max(abs(X[i]-X_max), abs(X[i]-X_min), abs(Y[i]-Y_max), abs(Y[i]-Y_min)))
ans.sort(reverse=True)
print(ans[2])
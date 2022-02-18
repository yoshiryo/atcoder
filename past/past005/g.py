import sys
sys.setrecursionlimit(5*10**5)

h,w = map(int,input().split())
S = [list(input()) for i in range(h)]

ans = []

def dfs(x,y,T):
    T[x][y] = "."
    ans.append((x,y))
    upd = 0
    for i,j in ((0,1),(1,0),(-1,0),(0,-1)):
        nx = x+i
        ny = y+j
        if 0 <= nx < h and 0 <= ny < w and T[nx][ny] == "#":
            upd = 1
            dfs(nx,ny,T)
    for t in T:
        if "#" in t:
            upd = 1
    if upd:
        T[x][y] = "#"
        ans.pop()
        return 0

    print(len(ans))
    for x,y in ans:
        print(x+1,y+1)
    exit()

for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            dfs(i,j,S)


    
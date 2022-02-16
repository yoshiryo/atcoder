n = int(input())
s = [list(input()) for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(1, 2*n - 2):
        if s[i][j] == "#":
            if s[i+1][j-1] == "X" or s[i+1][j] == "X" or s[i+1][j+1] == "X":
                s[i][j] = "X"
for i in s:
    print("".join(i))

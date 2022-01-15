n = int(input())
st = [input().split() for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if st[i][0] == st[j][0] and st[i][1] == st[j][1]:
            print("Yes")
            exit()
print("No")
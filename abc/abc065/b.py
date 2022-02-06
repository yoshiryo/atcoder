n = int(input())
a = [int(input()) for _ in range(n)]
np = a[0]
cnt = 1
for _ in range(n):
    if np == 2:
        print(cnt)
        exit()
    else:
        np = a[np-1]
        cnt += 1
print(-1)


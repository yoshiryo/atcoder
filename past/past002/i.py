n = int(input())
a = list(map(int, input().split()))
na = []
for i in range(2**n):
    na.append([a[i], i])
ans = [0]*2**n
cnt = 0
n = 2**n
while len(na) > 1:
    cnt += 1
    l = []
    if n == 2:
        index_x = na[0][1]
        index_y = na[1][1]
        ans[index_y] = cnt
        ans[index_x] = cnt
        break
    for i in range(0, n, 2):
        x = na[i][0]
        index_x = na[i][1]
        y = na[i+1][0]
        index_y = na[i+1][1]
        if x > y:
            l.append([x, index_x])
            ans[index_y] = cnt
        else:
            l.append([y, index_y])
            ans[index_x] = cnt
    na = l
    n //= 2
for i in ans:
    print(i)
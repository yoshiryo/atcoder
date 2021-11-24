n = int(input())
a = list(map(int, input().split()))
x = int(input())

su = sum(a)
if su > x:
    cnt = 0
    for i in range(n):
        cnt += a[i]
        if cnt > x:
            print(i+1)
            exit()
else:
    c = x//su
    ans = c*n
    cnt = 0
    x -= su*c
    for i in range(n):
        cnt += a[i]
        if cnt > x:
            print(i+1+ans)
            exit()
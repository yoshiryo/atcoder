t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    gin = [0]*(n+1)
    gout = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        gin[b] += 1
        gout[a] += 1
    ans = 0
    for i in range(1, n+1):
        if gin[i] > gout[i]:
            ans += gin[i] - gout[i]
    print(ans) 
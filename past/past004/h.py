n, m, k = map(int, input().split())
s = [input() for _ in range(n)]
mi = min(n, m)
for i in range(mi):
    ni = mi - i
    for h in range(n-ni+1):
        for w in range(m-ni+1):
            cnt = [0]*10
            for x in range(h, h+ni):
                for y in range(w, w+ni):
                    cnt[int(s[x][y])] += 1
            if ni**2 - max(cnt) <= k:
                print(ni)
                exit()

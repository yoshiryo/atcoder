n, m = map(int, input().split())
a = []
for _ in range(2 * n):
    s = input()
    a.append(s)
rank = [[0, i] for i in range(2 * n)]
for i in range(m):
    for j in range(n):
        p1 = rank[2 * j][1]
        p2 = rank[2 * j + 1][1]
        h1 = a[p1][i]
        h2 = a[p2][i]
        if h1 == h2:
            continue
        else:
            if h1 =="G":
                if h2 == "P":
                    rank[2 * j + 1][0] += 1
                else:
                    rank[2 * j][0] += 1
            elif h1 == "C":
                if h2 == "G":
                    rank[2 * j + 1][0] += 1
                else:
                    rank[2 * j][0] += 1
            else:
                if h2 == "C":
                    rank[2 * j + 1][0] += 1
                else:
                    rank[2 * j][0] += 1
        rank = sorted(rank, key=lambda x:x[1])
        rank = sorted(rank, key=lambda x:x[0], reverse=True)
for i in range(2 * n):
    print(rank[i][1] + 1)
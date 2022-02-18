from collections import Counter
n, K = map(int, input().split())
s = [input() for _ in range(n)]
c = Counter(s)
l = []
all = []
judge = True
for k, val in c.most_common():
    if judge:
        l.append(k)
        now_k = k
        now_val = val
        judge = False
    else:
        if now_val == val:
            l.append(k)
        else:
            all.append(l)
            l = []
            l.append(k)
            now_val = val
all.append(l)
for i in range(len(all)):
    l = all[i]
    if len(l) == 1 and K == 1:
        print(l[0])
        exit()
    elif len(l) >= K:
        print("AMBIGUOUS")
        exit()
    else:
        K -= len(l)

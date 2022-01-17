from itertools import product
n = int(input())
a = list(map(int, input().split())) 
bit = list(product([False, True], repeat=n-1))
mi = 10**10
for border in bit:
    l = []
    c = [a[0]]
    for i in range(n-1):
        if border[i] == True:
            cnt = 0
            for j in c:
                cnt |= j
            l.append(cnt)
            c = [a[i+1]]
        else:
            c.append(a[i+1])
    cnt = 0
    for k in c:
        cnt |= k
    l.append(cnt)
    ans = 0
    for k in l:
        ans ^= k
    mi = min(mi, ans)
print(mi)
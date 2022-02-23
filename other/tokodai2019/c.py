n, X = map(int, input().split())
A = list(map(int, input().split()))

x = X
ind = []
for i in range(n):
    if A[i] == -1:
        A[i] = 0
        ind.append(i)
    x ^= A[i]

if x == 0:
    print(*A)
elif len(ind) == 0:
    print(-1)
elif len(ind) == 1:
    if x <= X:
        A[ind[0]] = x
        print(*A)
    else:
        print(-1)
else:
    i1, i2 = ind[:2]
    y = x.bit_length() - 1
    if (1 << y) <= X:
        A[i1] = 1 << y
        A[i2] = x - (1 << y)
        print(*A)
    else:
        print(-1)

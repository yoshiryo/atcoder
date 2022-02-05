n = int(input())
l = [2, 1]
if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        c = l[i-2] + l[i-1]
        l.append(c)
    print(l[n])
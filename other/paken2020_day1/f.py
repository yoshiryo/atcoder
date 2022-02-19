p = int(input())
l = [1, 1]
if p == 1:
    print(1)
else:
    for i in range(2, 10**8):
        n = l[i-1] + l[i-2]
        if n%p == 0:
            print(i+1)
            exit()
        else:
            l.append(n)

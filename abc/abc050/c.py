from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(sorted(a))
mod = 10**9 + 7
if n%2 == 0:
    for i in range(n-1, 0, -2):
        if c[i] == 2:
            continue
        else:
            print(0)
            exit()
    print(2**(n//2)%mod)
else:
    for i in range(n-1, -1, -2):
        if i == 0:
            if c[0] == 1:
                continue
            else:
                print(0)
                exit() 
        else:
            if c[i] == 2:
                continue
            else:
                print(0)
                exit()
    print(2**(n//2)%mod)
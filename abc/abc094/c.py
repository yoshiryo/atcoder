n = int(input())
x = list(map(int, input().split()))
nx = sorted(x)
mid1 = nx[n//2 - 1]
mid2 = nx[n//2]
for i in range(n):
    if mid1 >= x[i]:
        print(mid2)
    else:
        print(mid1)


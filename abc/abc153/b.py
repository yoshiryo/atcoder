h, n = map(int, input().split())
a = list(map(int, input().split()))
all = sum(a)
if all >= h:
    print("Yes")
else:
    print("No")
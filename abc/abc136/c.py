n = int(input())
h = list(map(int, input().split()))
h = h[::-1]
now = h[0]
for i in range(1, n):
    if h[i] - now > 1:
        print("No")
        exit()
    elif h[i] - now == 1:
        now = h[i] - 1
    else:
        now = h[i]
print("Yes")
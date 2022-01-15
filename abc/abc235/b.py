n = int(input())
h = list(map(int, input().split()))
now = h[0]
for i in range(1, n):
    if now < h[i]:
        now = h[i]
    else:
        print(now)
        exit()
print(now)
n, m = map(int, input().split())
a = list(map(int, input().split()))
all = sum(a)
cnt = 0
for i in a:
    if i < all/(4*m):
        continue
    cnt += 1
if cnt >= m:
    print("Yes")
else:
    print("No")

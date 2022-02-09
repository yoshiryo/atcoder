n = int(input())
all = set()
ans = 0
for _ in range(n):
    a = int(input())
    if a in all:
        ans += 1
    all.add(a)
print(ans)
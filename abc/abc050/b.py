n = int(input())
t = list(map(int, input().split()))
m = int(input())
all = sum(t)
for _ in range(m):
    p, x = map(int, input().split())
    print(all - t[p-1] + x)
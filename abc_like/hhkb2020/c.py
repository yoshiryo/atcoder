n = int(input())
p = list(map(int, input().split()))
num = set()
now = 0
for i in range(n):
    num.add(p[i])
    while now in num:
        now += 1
    print(now)
n = int(input())
k = int(input())
now = 1
for _ in range(n):
    if now*2 > now + k:
        now += k
    else:
        now *= 2
print(now)
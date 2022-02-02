num = list(map(int, input().split()))
k = int(input())
for _ in range(k):
    num.sort()
    ma = num[-1]
    ma *= 2
    num = num[:-1] + [ma]
print(sum(num))
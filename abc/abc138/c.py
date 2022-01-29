n = int(input())
v = list(map(int, input().split()))
v.sort()
index = 1
now = v[0]
n -= 1
while n > 0:
    now = (now + v[index])/2
    index += 1
    n -= 1
print(now)
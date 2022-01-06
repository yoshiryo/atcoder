n = int(input())
a, b, c = map(int, input().split())
ans = 9999
for i in range(10000):
    for j in range(10000-i):
        re = (n - a*i - b*j) // c
        if a*i + b*j + c*re == n and re >= 0:
            ans = min(ans, i+j+re)
print(ans)
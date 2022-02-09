a = int(input())
ans = 0
for x in range(1, 100):
    for y in range(1, 100):
        if x + y == a:
            ans = max(ans, x*y)
print(ans)
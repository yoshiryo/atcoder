a, b = map(int, input().split())
for x in range(1, b+1):
    cnt = b//x - (a-1)//x
    if cnt >= 2:
        ans = x
print(ans)
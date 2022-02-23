n, p = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for x in a:
    if p >= x:
        p -= x
        cnt += 1
    else:
        break
print(cnt)

n = int(input())
s = input()
ans = 0
for i in range(1000):
    pw = str(i).zfill(3)
    cnt = 0
    for c in s:
        if c == pw[cnt]:
            cnt += 1
        if cnt == 3:
            ans += 1
            break
print(ans)
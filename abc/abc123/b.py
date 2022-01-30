import itertools 
dishe = [int(input()) for _ in range(5)]
ans = 10**10
for ld in itertools.permutations(dishe):
    cnt = 0
    for i in range(5):
        if i != 4:
            if ld[i]%10 == 0:
                cnt += ld[i]
            else:
                cnt += 10*(ld[i]//10 + 1)
        else:
            cnt += ld[i]
    ans = min(ans, cnt)
print(ans)
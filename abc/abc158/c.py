a, b = map(int, input().split())
ans = 1
while ans <= 1009:

    if int(ans * 0.08) == a and int(ans * 0.1) == b:
        print(ans)
        exit()
    else:
        ans += 1
print(-1)
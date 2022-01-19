n = int(input())
cnt = 0
for i in range(1, n+1):
    num10 = str(i)
    num8 = oct(i)
    if "7" not in num10 and "7" not in num8:
        cnt += 1
print(cnt)
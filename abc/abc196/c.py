n = int(input())
cnt = 0
num = 1
while True:
    s = str(num)*2
    x = int(s)
    if x <= n:
        cnt += 1
    else:
        break
    num += 1
print(cnt)

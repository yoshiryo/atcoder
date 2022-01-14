n = int(input())
cnt = 0
for i in range(1, 10**9):
    cnt += i
    if cnt >= n:
        print(i)
        break

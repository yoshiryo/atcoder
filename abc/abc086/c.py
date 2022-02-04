n = int(input())
now_x = 0
now_y = 0
now_time = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    d = abs(now_x - x) + abs(now_y - y)
    dt = abs(now_time - t)
    if dt < d or dt%2 != d%2:
        print("No")
        exit()
    now_x = x
    now_y = y
    now_time = t
print("Yes")
x, y = map(int, input().split())
if x > y:
    print(0)
else:
    diff = y - x
    print((diff + 10 - 1) // 10)
x, y = map(int, input().split())
if y == 0:
    print("ERROR")
else:
    xy = 100*x//y/100
    print('{:.2f}'.format(xy))
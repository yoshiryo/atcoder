x1, y1, x2, y2 = map(int, input().split())
x1y1 = [[x1+1, y1+2], [x1+2, y1+1], [x1+2, y1-1], [x1+1, y1-2],
        [x1-1, y1-2], [x1-2, y1-1], [x1-2, y1+1], [x1-1, y1+2]]
x2y2 = [[x2+1, y2+2], [x2+2, y2+1], [x2+2, y2-1], [x2+1, y2-2],
        [x2-1, y2-2], [x2-2, y2-1], [x2-2, y2+1], [x2-1, y2+2]]
for xy in x1y1:
    if xy in x2y2:
        print("Yes")
        exit()
print("No")

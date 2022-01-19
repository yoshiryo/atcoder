x, y = map(int, input().split())
diff = abs(x - y)

if diff < 3:
    print("Yes")
else:
    print("No")
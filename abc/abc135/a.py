a, b = map(int, input().split())
diff = abs(a - b)
if diff%2 == 0:
    print(min(a, b) + diff//2)
else:
    print("IMPOSSIBLE")
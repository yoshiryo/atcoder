a, b, c = map(int, input().split())
l = [[a, "A"], [b, "B"], [c, "C"]]
l = sorted(l, key=lambda x:x[0])
print(l[1][1])
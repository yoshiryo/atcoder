num = list(map(int, input().split()))
if num.count(5) == 2 and num.count(7) == 1:
    print("YES")
else:
    print("NO")
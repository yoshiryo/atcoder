n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n-1):
    if a[i+1] > a[i]:
        print("up", a[i+1] - a[i])
    elif a[i+1] == a[i]:
        print("stay")
    else:
        print("down", a[i] - a[i+1])
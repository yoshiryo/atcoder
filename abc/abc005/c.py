t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
if n < m:
    print("no")
else:
    for bi in b:
        judge = False
        for i in range(n):
            if bi - t <= a[i] <= bi and a[i] != -1:
                judge = True
                a[i] = -1
                break
        if not judge:
            print("no")
            exit()
    print("yes")
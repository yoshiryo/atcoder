n = int(input())
a = list(map(int, input().split()))
a = set(a)
if n == len(a):
    print("YES")
else:
    print("NO")
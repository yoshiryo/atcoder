n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        print(-1)
    else:
        print(abs(a-b))
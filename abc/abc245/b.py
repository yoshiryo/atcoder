n = int(input())
a = list(map(int, input().split()))
a = set(a)
for i in range(3000):
    if i not in a:
        print(i)
        exit()
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans1 = 0
ans2 = 0
for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            if i == j:
                ans1 += 1
            else:
                ans2 += 1
print(ans1)
print(ans2)
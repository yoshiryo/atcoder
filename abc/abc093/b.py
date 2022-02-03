a, b, k = map(int, input().split())
ans = []
for i in range(a, b+1):
    if i < a+k or b-k < i:
        ans.append(i)
for i in ans:
    print(i)
n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a*b, a, b, i+1])
ab = sorted(ab, key=lambda x:x[0], reverse=True)
top_a, top_b, ans = ab[0][1:]
for i in range(1, n):
    a, b =ab[i][1:3]
    if (top_a + b - 1)//b <= (a + top_b - 1)//top_b:
        ans = -1
        break
print(ans)
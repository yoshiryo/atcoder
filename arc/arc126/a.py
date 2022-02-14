t = int(input())
for _ in range(t):
    n2, n3, n4 = map(int, input().split())
    ans = 0
    if n3 >= 2 and n4 >= 1:
        cnt = min(n3//2, n4)
        ans += cnt
        n3 -= cnt*2
        n4 -= cnt
    if n2 >= 1 and n4 >= 2:
        cnt = min(n2, n4//2)
        ans += cnt
        n2 -= cnt
        n4 -= cnt*2
    if n2 >= 2 and n3 >= 2:
        cnt = min(n2//2, n3//2)
        ans += cnt
        n2 -= cnt*2
        n3 -= cnt*2
    if n2 >= 3 and n4 >= 1:
        cnt = min(n2//3, n4)
        ans += cnt
        n2 -= cnt*3
        n4 -= cnt
    if n2 >= 5:
        cnt = n2//5
        ans += cnt
    
    print(ans)
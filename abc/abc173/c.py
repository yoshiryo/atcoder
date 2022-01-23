from itertools import product 
h, w, k = map(int, input().split())
c = [input() for _ in range(h)]
l_h = list(product([False, True], repeat=h))
l_w = list(product([False, True], repeat=w))
ans = 0
for row_bit in l_h:
    for col_bit in l_w:
        cnt = 0
        for i in range(h):
            for j in range(w):
                if row_bit[i] == False and col_bit[j] == False:
                    if c[i][j] == "#":
                        cnt += 1
        if cnt == k:
            ans += 1
print(ans)
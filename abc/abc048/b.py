a, b, x = map(int, input().split())
if a%x == 0:
    a_cnt= a//x - 1
else:
    a_cnt = a//x
b_cnt = b//x
print(b_cnt - a_cnt)
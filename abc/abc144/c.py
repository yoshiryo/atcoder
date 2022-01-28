import math
n = int(input())
mid = int(math.sqrt(n))
ans = 10**13
for i in range(1, mid+1):
    if n%i == 0:
        a = i
        b = n//i
        ans = min(ans, a-1 + b-1)
print(ans)
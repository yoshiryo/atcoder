import math
a, b, c = map(int, input().split())
k = math.gcd(a, math.gcd(b, c))
ans = a//k + b//k + c//k - 3
print(ans)
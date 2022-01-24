a, b, n = list(map(int, input().split()))
x = min(b - 1, n) 
ans = int(a * x / b) 
print(ans)
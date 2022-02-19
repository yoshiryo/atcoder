def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())
for x in range(a, b+1):
    judge = True
    for y in range(c, d+1):
        su = x+y
        if is_prime(su):
            judge = False
            break
    if judge:
        print("Takahashi")
        exit()
print("Aoki")

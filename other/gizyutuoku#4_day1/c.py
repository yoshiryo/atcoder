def Base_10_to_n(x, n):
    if x//n:
        return Base_10_to_n(x//n, n)+str(x%n)
    else:
        return str(x%n)

N, x = map(int, input().split())

for i in range(2,11):
    t = Base_10_to_n(N,i)
    if t == str(x):
        print(i)
        break
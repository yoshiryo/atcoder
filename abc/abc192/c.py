n, k = map(int, input().split())

def g1(x1):
    x1 = list(str(x1))
    x1.sort(reverse=True)
    return int(''.join(x1))
def g2(x2):
    x2 = list(str(x2))
    x2.sort()
    return int(''.join(x2))
def f(x):
    return g1(x) - g2(x)

for i in range(k):
    n = f(n)
print(n)

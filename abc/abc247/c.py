def s(n):
    if n == 1:
        return "1"
    if n == 2:
        return "1 2 1"
    else:
        return s(n-1) + " " + str(n) + " " + s(n-1)

n = int(input())
print(s(n))
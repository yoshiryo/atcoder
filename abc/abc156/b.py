def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out
n, k = map(int, input().split())
n = Base_10_to_n(n, k)
print(len(n))
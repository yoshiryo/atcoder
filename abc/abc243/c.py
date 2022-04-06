n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
s = input()

r_min = dict()
l_max = dict()

for i in range(n):
    if s[i] == "R":
        if Y[i] in l_max and X[i] < l_max[[Y[i]]]:
            print("Yes")
            exit()
    else:
        if Y[i] in r_min and r_min[Y[i]] < X[i]:
            print("Yes")
            exit()
    if s[i] == "R":
        if Y[i] in r_min:
            r_min[Y[i]] = min(X[i], r_min[Y[i]])
        else:
            r_min[Y[i]] = X[i]
    else:
        if Y[i] in l_max:
            l_max[Y[i]] = max(X[i], l_max[[Y[i]]])
        else:
            l_max = X[i]
print("No")    
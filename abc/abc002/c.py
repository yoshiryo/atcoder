xa, ya, xb, yb, xc, yc = map(int, input().split())
dx_ab = xb - xa
dy_ab = yb - ya
dx_ac = xc - xa
dy_ac = yc - ya
print(abs(dx_ab * dy_ac - dx_ac * dy_ab)/2)
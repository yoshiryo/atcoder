c = [list(map(int, input().split())) for _ in range(3)]
if c[0][0] - c[0][1] == c[1][0] - c[1][1] and c[0][0] - c[0][1] == c[2][0] - c[2][1]:
    if c[0][0] - c[0][2] == c[1][0] - c[1][2] and c[0][0] - c[0][2] == c[2][0] - c[2][2]:
        if c[0][1] - c[0][2] == c[1][1] - c[1][2] and c[0][1] - c[0][2] == c[2][1] - c[2][2]:
            print("Yes")
            exit()
print("No")
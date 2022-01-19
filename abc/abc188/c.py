n = int(input())
a = list(map(int, input().split()))
player = []
for i in range(2**n):
    player.append([i+1, a[i]])

for i in range(n-1):
    win = []
    for j in range(0, len(player), 2):
        if player[j][1] > player[j+1][1]:
            win.append(player[j])
        else:
            win.append(player[j+1])
    player = win

player = sorted(player, key=lambda x:x[1])
print(player[0][0])
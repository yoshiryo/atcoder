a, b = input().split()
mi = min(len(a), len(b))

for i in range(mi):
    num_a = int(a[len(a) - (i+1)])
    num_b = int(b[len(b) - (i+1)])
    if num_a + num_b >= 10:
        print("Hard")
        exit()
print("Easy")
n = int(input())
h = n//3600
n -= h*3600
m = n//60
n -= m*60
print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(n).zfill(2))
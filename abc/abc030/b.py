n, m = map(int, input().split())
short = m/60*360%360
long = (n/12*360 + m/60*30)%360
ma = max(long, short)
mi = min(long, short)
print(min((ma - mi), 360-ma+mi))
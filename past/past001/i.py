INF=10**18
def main():
    N,M=map(int,input().split())
    dp=[INF]*(1<<N)
    dp[0]=0
    for _ in range(M):
        s,c=input().split()
        s=int(s.replace('Y','1').replace('N','0'),2)
        c=int(c)
        for i in range(1<<N):
            j=i|s
            x=dp[i]+c
            if dp[j]>x:
                dp[j]=x
    print(dp[-1] if dp[-1]!=INF else -1)
main()
t=int(input())
for _ in range(t):
    x, n=map(int,input().split())
    r=n%4
    if(r==0):
        ans=x
    elif(r==1):
        ans=x-n
    elif(r==2):
        ans=x-1
    else:
        ans=x+n+1
    print(ans)
    
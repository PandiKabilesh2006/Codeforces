t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if(a==n and b==n):
        print("YES")
    elif(a+b<=n-2):
        print("YES")
    else:
        print("NO")
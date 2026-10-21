t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x=(2*b-c)/a
    y=(a+c)/(2*b)
    z=(2*b-a)/c
    if(any(v>0 and v.is_integer() for v in [x,y,z])):
        print("YES")
    else:
        print("NO")
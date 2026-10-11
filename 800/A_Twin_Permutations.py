t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[n+1-x for x in a]
    print(*b)
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    xor=0
    for num in nums:
        xor^=num
    if(n%2==1):
        print(xor)
    else:
        if(xor==0):
            print(0)
        else:
            print(-1)
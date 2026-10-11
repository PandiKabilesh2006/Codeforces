t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    current=0
    maxi=0
    for num in nums:
        if(num==0):
            current+=1
            maxi=max(maxi,current)
        else:
            current=0
    print(maxi)
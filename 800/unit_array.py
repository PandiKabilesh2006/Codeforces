t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    total=sum(nums)
    minus=0
    for i in range(n):
        if(nums[i]==-1):
            minus+=1
    ans=0
    while(total<0 or minus%2!=0):
        if(total<0):
            total+=2
            minus-=1
            ans+=1
        else:
            total+=2
            minus-=1
            ans+=1
    print(ans)

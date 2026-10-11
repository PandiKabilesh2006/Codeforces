t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    ans=0
    curr=0
    for num in nums:
        if(num==0):
            if(curr!=0):
                ans+=1
                curr=0
        else:
            curr+=1
    if(curr!=0):
        ans+=1
    print(min(ans,2))

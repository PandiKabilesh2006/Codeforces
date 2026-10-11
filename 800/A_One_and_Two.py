t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    prod=1
    for num in nums:
        prod*=num
    running=1
    ans=-1
    for k in range(n-1):
        running*=nums[k]
        if(running==prod/running):
            ans=k+1
            break
    print(ans)

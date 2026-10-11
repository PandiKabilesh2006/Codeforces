t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    ans=float('-inf')
    ans=max(ans,nums[-1]-nums[0])
    ans=max(ans,max(nums)-nums[0])
    ans=max(ans,nums[-1]-min(nums))
    for i in range(n):
        ans=max(ans,nums[i]-nums[(n+i+1)%n])
    print(ans)
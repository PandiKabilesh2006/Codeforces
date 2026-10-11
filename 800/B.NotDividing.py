t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    for i in range(n):
        if(nums[i]==1):
            nums[i]=nums[i]+1
    for i in range(n-1):
        if(nums[i+1]%nums[i]==0):
            nums[i+1]+=1
    print(*nums)

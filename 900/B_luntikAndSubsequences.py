t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    ones=nums.count(1)
    zeros=nums.count(0)
    if(zeros==0):
        print(ones)
    else:
        print(ones*(2**zeros))
    # target=sum(nums)-1
    # def recursion(ind, total):
    #     if(ind==n):
    #         if(total==target):
    #             return 1
    #         return 0
    #     take=recursion(ind+1, total+nums[ind])
    #     nottake=recursion(ind+1, total)
    #     return take+nottake
    # ans=recursion(0,0)
    # print(ans)
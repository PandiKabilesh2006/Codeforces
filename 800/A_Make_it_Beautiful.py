t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    maxi=nums[-1]
    mini=nums[0]
    if(maxi==mini):
        print("NO")
    else:
        print("YES")
        print(maxi, *nums[:-1])
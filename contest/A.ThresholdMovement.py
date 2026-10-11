t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    if(n%2!=0):
        print("NO")
        continue
    minOdd=float('inf')
    maxEven=-float('inf')
    for i in range(n):
        if((i+1)%2==1):
            minOdd=min(minOdd,nums[i])
        else:
            maxEven=max(maxEven,nums[i])
    if(minOdd-maxEven>=2):
        print("YES")
    else:
        print("NO")


from math import gcd
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    possible=False
    for i in range(n):
        for j in range(i+1,n):
            if(gcd(nums[i],nums[j])<=2):
                possible=True
                break
        if(possible):
            break
    print("YES" if possible else "NO")


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    left=0
    right=n-1
    while(left<right):
        if((s[left]=='0' and s[right]=='0') or (s[left]=='1'  and s[right]=='1')):
            break
        else:
            left+=1
            right-=1
    print(right-left+1)

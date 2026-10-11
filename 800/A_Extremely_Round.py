t=int(input())
for _ in range(t):
    n=int(input())
    digits=0
    num=n
    ans=0
    while(num>0):
        digits+=1
        digit=num%10
        num//=10
    ans+=(digits-1)*9
    ans+=(n//(10**(digits-1)))
    print(ans)
    
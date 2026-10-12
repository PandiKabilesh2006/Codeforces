t=int(input())
for _ in range(t):
    n=int(input())
    if(n<4 or n%2==1):
        print(-1)
    else:
        mini=(n+5)//6
        maxi=n//4
        print(mini, maxi)
        # if(n%6==0 and n%4==0):
        #     mini=n//6
        #     # maxi=(n-6)//4+1
        #     maxi=n//4
        # elif(n%6==0):
        #     mini=n//6
        #     maxi=(n-6)//4+1
        # elif(n%4==0):
        #     maxi=n//4
        #     if(n%6==2):
        #         mini=(n-8)//6+2
        #     elif(n%6==4):
        #         mini=(n-4)//6+1
        # else:
        #     mini=(n-4)//6+1
        #     maxi=(n-6)//4+1
        # print(mini, maxi)
t=int(input())
for _ in range(t):
    n=input().strip()
    ans=len(n)
    endings=['00','50','25','75']
    for ending in endings:
        first, second=ending[0], ending[1]
        for i in range(len(n)-1,-1,-1):
            if(n[i]==second):
                for j in range(i-1,-1,-1):
                    if(n[j]==first):
                        ans=min(ans, len(n)-j-2)
    print(ans)
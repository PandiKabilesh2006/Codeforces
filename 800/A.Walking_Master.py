t=int(input())
for _ in range(t):
    sr,sc,dr,dc=map(int,input().split())
    if(sc==dc):
        if(sr>=dr):
            print(sr-dr)
        else:
            print(-1)
    elif(sc>dc):
        print(-1)
    else:
        step=dc-sc
        nr=sr+step
        if(nr-dr>=0):
            print(step+(nr-dr))
        else: 
            print(-1)

# from functools import lru_cache
# t=int(input())
# for _ in range(t):
#     a,b,c,d=map(int,input().split())
#     @lru_cache(None)
#     def recursion(ind1,ind2):
#         if(ind1==c and ind2==d):
#             return 0
#         moves=float('inf')
#         if(ind2>d):
#             return float('inf')
#         if(ind2<d):
#             moves=min(moves,1+recursion(ind1+1,ind2+1))
#         if(ind1>c):
#             moves=min(moves,1+recursion(ind1-1,ind2))

#         return moves
#     ans=recursion(a,b)
#     if(ans!=float('inf')):
#         print(ans)
#     else:
#         print(-1)

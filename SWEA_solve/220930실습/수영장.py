T=int(input())
for tc in range(1,T+1):
    dcost,mcost,tmcost,ycost = map(int,input().split())
    plan=[0]+list(map(int,input().split()))
    cost=[0]*13
    for i in range(1,13):
        cost[i]=min(dcost*plan[i],mcost)+cost[i-1]
        if i>=3: #3개월
            cost[i]=min(cost[i],tmcost+cost[i-3])
        if i==12:
            cost[i]=min(cost[i],ycost) 
    print(f'#{tc} {cost[-1]}')
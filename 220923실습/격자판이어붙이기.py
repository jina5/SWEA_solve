T=int(input())

di=[-1,1,0,0] #상하좌우
dj=[0,0,-1,1] 
def solve(start,case,cnt):
    i,j=start
    if cnt==6:
        if case not in result:
            result.append(case)
        return
    
    for d in range(4):
        ni = i+di[d]
        nj = j+dj[d]    
        if 0<=ni<4 and 0<=nj<4:
            tmp = case + arr[ni][nj]
            solve((ni,nj),tmp,cnt+1)
    return
        
for tc in range(1,T+1):
    arr=list(input().split() for _ in range(4))
    result=[]
    for i in range(4):
        for j in range(4):
            solve((i,j),arr[i][j],0)
    print(f'#{tc} {len(result)}')
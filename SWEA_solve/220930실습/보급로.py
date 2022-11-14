d=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
def bfs(ni,nj):
    q=[]
    q.append((ni,nj))
    visited[0][0]=0
    while q :
        ni,nj = q.pop(0)
        for i in range(4):
            newi=ni+d[i][0]
            newj=nj+d[i][1]       
            if 0<=newi<n and 0<=newj<n:
                if visited[newi][newj]>visited[ni][nj]+int(arr[newi][newj]):
                    visited[newi][newj]=visited[ni][nj]+int(arr[newi][newj])
                    q.append((newi,newj))                
    return visited[n-1][n-1]    
T=int(input())
for tc in range(1,T+1):
    n= int(input())
    arr= [input() for _ in range(n)]
    visited=[[1e9]*n for _ in range(n)]
    print(f'#{tc} {bfs(0,0)}')
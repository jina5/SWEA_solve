di=[-1,1,0,0] #상하좌우
dj=[0,0,-1,1]

def bfs(ni,nj):
    q = [(ni,nj)]
    visited[0][0]=0
    while q :
        ni,nj = q.pop(0)
        for i in range(4):
            newi=ni+di[i]
            newj=nj+dj[i]
            cost=1
            if 0<=newi<n and 0<=newj<n:
                if arr[newi][newj]>arr[ni][nj]:
                    cost=1+arr[newi][newj]-arr[ni][nj]
                if visited[ni][nj]+cost < visited[newi][newj]:         
                    q.append((newi,newj))
                    visited[newi][newj]=visited[ni][nj]+cost
    return visited[n-1][n-1]

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    visited=[[1e9]*n for _ in range(n)]
    print(f'#{tc} {bfs(0,0)}')
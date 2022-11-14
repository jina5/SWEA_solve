def prim(start, V):
    MST = [0]*(V+1)    
    key = [10]*(V+1) 
    key[start] = 0          
    for _ in range(V):  
        u = 0
        minV = 10
        for i in range(V+1):
            if MST[i]==0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1               
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])     # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)  

T=int(input())
for tc in range(1,T+1):
    v,e= map(int,input().split())
    adjM = [[0]*(v+1) for _ in range(v+1)]
    for i in range(v+1):
        adjM[i][i] = 0
    for _ in range(e):
        n1,n2,w=map(int,input().split())
        adjM[n1][n2]=w
        adjM[n2][n1]=w
    print(f'#{tc} {prim(0,v)}')
        
    
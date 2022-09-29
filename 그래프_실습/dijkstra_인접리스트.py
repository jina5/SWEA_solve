def dijkstra(s, N):
    U = [0]*(N+1)       
    U[s] = 1            
    D[s] = 0
    for v, w in adjL[s]:
        D[v] = w

    for _ in range(N):     
        minV = INF
        t = 0
        for i in range(N+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        U[t] = 1              
        for v, w in adjL[t]:
                D[v] = min(D[v], D[t]+w)
T=int(input())
for tc in range(1,T+1):
    INF = 10000
    N, E = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjL[u].append([v, w])

    D = [INF]*(N+1)
    dijkstra(0, N)
    print(f'#{tc} {D[N]}')
import heapq
 
INF = 1e9
 
def diji(i):
    distance = [INF] * (n**2)
    q = []
    heapq.heappush(q, (0, i))
    distance[i] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] > dist:
            continue
        for i in graph_second[node]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance[-1]
     
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    num = []
    for i in range(1, n+1):
        num.append([j for j in range(i*n - n, i*n)])
    graph_second = [[]for _ in range(n*n)]
     
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
     
    for i in range(n):
        for j in range(n):
            for k in range(4):
                x = j + dx[k]
                y = i + dy[k]
                if 0 <= x < n and 0 <= y < n:
                    oil = graph[i][j] - graph[y][x] if graph[i][j] - graph[y][x] < 0 else 0
                    value = 1 - oil
                    graph_second[num[i][j]].append((value, num[y][x]))
    print(f'#{tc} {diji(0)}')
import heapq
INF = 1e9
 
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
 
def diji():
    distance = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        cost, y, x = heapq.heappop(q)
         
        if distance[y][x] < cost:
            continue
         
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                new_cost = graph[ny][nx] + cost
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heapq.heappush(q, (new_cost, ny, nx))
    return distance[-1][-1]
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = []
    for _ in range(n):
        arr = list(input())
        graph.append(list(map(int, arr)))
     
     
    print(f'#{tc} {diji()}')
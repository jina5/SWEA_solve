import heapq
v=5
e=4
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
def prim(start):
    visit = [0] * (v+1)
    q = []
    for i in graph[start]:
        heapq.heappush(q, i)
    mst = [start]
    total_cost = 0
    visit[start] = 1
    while q:
        c, node = heapq.heappop(q)
        if visit[node] == 0:
            visit[node] = 1
            mst.append(node)
            total_cost += c
            
            for edge in graph[node]:
                if visit[edge[1]] == 0:
                    heapq.heappush(q, edge)
    return total_cost
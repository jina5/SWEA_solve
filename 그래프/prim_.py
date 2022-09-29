# 1. 최소 비용 노드선택
# 2. 각 노드로 가는 최소비용 업데이트
# 1,2 번 반복
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
V, E = map(int,input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e, weight = map(int,input().split())
    adj[s][e] = weight
    adj[e][s] = weight

# prim 시작
# 각 노드로 갈 수 있는 비용을 저장하는 배열
mst = set()
mst_value = 0
weights = [0xfffffff] * (V+1)
#시작 정점은 0번으로
weights[0] = 0
# 모든 노드들이 선택될 때 까지 반복
while len(mst) <= V:
    min_v = 0xfffffff
    min_idx = 0
    for i in range(V+1):
        if i not in mst and weights[i] < min_v :
            min_idx = i
            min_v = weights[i]
    # 반복문을 다 돌고 나면, 최소 비용으로 갈 수 있는 노드가 선택됨
    # 선택된 노드를 MST에 추가하고,
    mst.add(min_idx)
    mst_value += min_v

    # 그 노드로 부터 다른 노드로 갈수 있는 비용을 확인하고, 기존 비용보다
    # 더 적다면, 업데이트
    for i in range(V+1):
        if i not in mst and adj[min_idx][i] and adj[min_idx][i] < weights[i]:
            weights[i] = adj[min_idx][i]

print(mst_value)











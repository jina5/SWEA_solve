# r,c 현재위치
# dir : 움직이는 방향
# visited : 방문했던 카페에서 파는 디저트 set
# 한바퀴 돌아서 다시 도착한 경우를 검사하기 위해서 visited 검사
# 시작지점은 visited가 비어 있을것..
# 투어가 완료된 상태 먹은 디저트 검사
# 도착한 곳에서 파는 디저트가 먹어본거다 >> 끝
# 직진또는 다음방향이동
# 직진이동
# 방향전환 (한방향으로)


def dfs(r,c, dir,visited):
    global max_value
    if visited and (r,c) == (i,j):
        if max_value < len(visited):
            max_value = len(visited)
        return
    if r < 0 or r >= N or c < 0 or c >= N or data[r][c] in visited:
        return
    visited.add(data[r][c])
    dfs(r+dr[dir], c+dc[dir],dir,visited)
    if dir < 3:
        dfs(r + dr[dir+1], c + dc[dir+1], dir+1, visited)
    visited.remove(data[r][c])

dr = [1,1,-1,-1]
dc = [1,-1,-1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    max_value = 0
    for i in range(N):
        for j in range(N):
            dfs(i,j,0,set())
    print(f'#{tc} {max_value    if max_value > 0 else -1}')
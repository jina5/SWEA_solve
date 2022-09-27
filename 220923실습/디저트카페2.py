def solve(x,y,cnt,i):
    global a, b
    for i in range(i,4): #i방향부터!
        dr = x + dx[i]
        dc = y + dy[i]
        if 0 <= dr < N and 0 <= dc < N:
            if not visited[case[dr][dc]] and not check[dr][dc]:
                visited[case[dr][dc]] = 1
                check[dr][dc] = 1
                solve(dr,dc,cnt+1,i)
                visited[case[dr][dc]] = 0
                check[dr][dc] = 0
        if dr == a and dc == b and cnt > 3:
            lst.append(cnt)
 
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    case = [list(map(int,input().split())) for _ in range(N)]
 
    dx = [1,1,-1,-1]
    dy = [1,-1,-1,1]
    # 우밑 / 좌밑 / 좌상 / 우상
    lst = []
    for i in range(N):
        for j in range(N):
            visited = [0] * 101
            visited[case[i][j]] = 1
            check = [[0] * N for _ in range(N)]
            check[i][j] = 1
            a ,b = i, j
            solve(i,j,1,0)
    if lst:
        print(f'#{tc} {max(lst)}')
    else:
        print(f'#{tc} -1')
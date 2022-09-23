dx=[-1, 1, 0, 0] #상하좌우
dy=[0, 0, -1, 1]

def search(i,j):
    global N
    cnt = 1
    stack = [(i,j)]
    while stack:
        x,y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] + 1 == arr[nx][ny]:
                    cnt += 1
                    stack.append((nx,ny))
    return cnt



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    max_start=0
    max_go=0
    for i in range(N):
        for j in range(N):
            cnt = search(i, j)
            if cnt > max_go:
                max_go = cnt
                max_start = arr[i][j]
                
            #이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.
            elif cnt == max_go:
                if arr[i][j] < max_start:
                    max_go=cnt
                    max_start = arr[i][j]

    print(f'#{tc} {max_start} {max_go}')
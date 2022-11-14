'''
맨 왼 쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록
움직였다면 이때의 합계를 출력하세요
 
- 오른쪽이나 아래로만 이동 가능
'''
# pos : position, sm : sum
def search(pos, sm):
    global ans
    r = pos[0]
    c = pos[1]
    # 최우측하단 부에 도착했을 때
    if pos == ((N-1),(N-1)):
        if sm < ans:
            ans = sm
        return
 
    # 아래, 오른
    dr = [1, 0]
    dc = [0, 1]
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if N > nr >= 0 and N > nc >= 0:
            new_pos = (nr, nc)
            search(new_pos, sm+lst[nr][nc])
    return None
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    start = end = 0
    pos = (start, end)
    sm = lst[0][0]
    search(pos, sm)
    print(f'#{tc} {ans}')
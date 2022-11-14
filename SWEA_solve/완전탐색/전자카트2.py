def f(n,sum_data,cnt):
    global N
    if cnt == N-1:
        sum_data += data[n][0]
        sum_lst.append(sum_data)
 
    else:
        for i in range(1,N):
            if not visited[i]:
                visited[i] = 1
                sum_data += data[n][i]
                f(i,sum_data,cnt+1)
                visited[i] = 0
                sum_data -= data[n][i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    sum_lst = []
    f(0,0,0)
    print(f'#{tc} {min(sum_lst)}')
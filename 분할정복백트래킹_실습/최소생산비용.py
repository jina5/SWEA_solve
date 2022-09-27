def solve(n,total):
    global ans
    if n==N:
        if total<ans:
            ans=total
        return
    if total>ans:
        return
    for j in range(N):
        if not visited[j]:
            visited[j]=1
            solve(n+1,total+arr[n][j])   
            visited[j]=0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited=[0]*N
    ans=10e9
    solve(0,0)
    print(f'#{tc} {ans}')
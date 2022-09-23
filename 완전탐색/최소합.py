def dfs(i, j, total):
    global min_sum
    if total > min_sum:
        return
    if i == n - 1 and j == n - 1:
        if min_sum > total:
            min_sum=total
        return
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if ni < n and nj < n:
            dfs(ni, nj, total + arr[ni][nj])


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    delta = ((1, 0), (0, 1))
    min_sum=0
    for a in arr:
        min_sum+=sum(a)
    total=arr[0][0]
    dfs(0, 0, total)
    print(f'#{tc} {min_sum}')
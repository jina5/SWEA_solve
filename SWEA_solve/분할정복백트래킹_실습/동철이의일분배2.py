def divide(n):
    return int(n)/100

def solve(i, per, idx):
    global ans

    if per <= ans:
        return

    if i == n-1:
        ans = max(ans, per)
        return

    for j in range(n):
        if not check[j]:
            check[j] = 1
            solve(i+1, per*arr[idx+1][j], idx+1)
            check[j] = 0

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(divide, input().split())) for _ in range(n)]
    check = [0] * n
    ans = 0
    for i in range(n):
        check[i] = 1
        solve(0, arr[0][i], 0)
        check[i] = 0
    ans = ans * 100

    print(f'#{tc}', end=' ')
    print('%.6f' % ans)
def solve(i,per):
    global ans
    if i==n:
        if per > ans:
            ans = per
        return
    if per <= ans :
        return
    for j in range(n):
        if not check[j]:
            check[j]=1
            result=per*(arr[i][j])
            solve(i+1,result)
            check[j]=0

def to_rate(num):
    return int(num)/100


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr = [list(map(to_rate, input().split())) for _ in range(n)]
    check=[0]*n
    ans=0
    solve(0,1)
    ans=ans*100
    print(f'#{tc}', end=' ')
    print('%.6f'%ans)
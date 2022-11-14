def solve(start,cnt):
    global ans
    if start>=n-1:
        if cnt<ans:
            ans=cnt
        return
    if cnt > ans: 
        return
    for i in range(1,1+arr[start]):
        solve(start+i,cnt+1)   
T=int(input())
for tc in range(1,T+1):
    n,*arr=map(int,input().split())
    ans=n
    solve(0,-1)
    print(f'#{tc} {ans}')

    
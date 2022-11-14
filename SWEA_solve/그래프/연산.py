def dfs(n,cnt): #maximum recursion
    global ans
    oper=[n+1,n-2,n*2,n-10]
    if n < 0 or n>1000000:
        return
    if n==m:
        return min(ans,cnt)
    for i in range(4):
        n=oper[i]
        cnt+=1
        dfs(n,cnt)
def bfs(n):
    q = [(n,0)]
    v[n]=1
    while q :
        n, cnt = q.pop(0)
        oper=[n+1,n-1,n*2,n-10]
        if n == m :
            return cnt 
        for i in range(4):
            n=oper[i]
            if 0<=n<=1000000 and not v[n]:
                v[n]=1
                q.append((n,cnt+1))

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    v=[0]*10000001
    print(f'#{tc} {bfs(n)}')

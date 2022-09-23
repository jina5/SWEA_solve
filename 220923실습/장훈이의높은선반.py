T=int(input())
def nCr(n, r, s):
    if r == 0:
        total=sum(comb)
        if total>=b:
            can.append(sum(comb))
    else:
        for i in range(s, n-r+1):
            comb[r-1] = tall[i]
            nCr(n, r-1, i+1)

for tc in range(1,T+1):
    n,b=map(int,input().split())
    tall=list(map(int,input().split()))
    can=[]
    for r in range(1,n+1):
        comb = [0] * r
        nCr(n, r, 0)
    can.sort()
    print(f'#{tc} {can[0]-b}')
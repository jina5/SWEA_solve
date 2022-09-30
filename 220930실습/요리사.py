def nCr(n, r, s): 
    global total
    if r == 0:
        comb2=set(comb)
        el=set(A)-comb2
        el=list(el)
        comb2=list(comb2)
        temp1=0
        temp2=0
        for i in el:
            for j in el:
                if i!=j:
                    temp1+=arr[i][j]
        for i in comb2:
            for j in comb2:
                if i!=j:
                    temp2+=arr[i][j]
        if total>abs(temp1-temp2):
            total=abs(temp1-temp2)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    A=[i for i in range(n)]
    r = n//2
    comb = [0] * r
    total=10000000
    nCr(n, r, 0)
    print(f'#{tc} {total}')

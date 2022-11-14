def a(l,r,c,lr):
    global cnt
    m = (l+r)//2
    if A_lst[m] == c:
        cnt += 1
        return
    elif c < A_lst[m]:
        if lr == 'l':
            return
        else:
            lr = 'l'
            a(l,m-1,c,lr)
    elif A_lst[m] < c:
        if lr == 'r':
            return
        else:
            lr = 'r'
            a(m+1,r,c,lr)


T = int(input())

for tc in range(1,T+1):
    A, B = map(int,input().split())
    A_lst = sorted(list(map(int,input().split())))
    B_lst = list(map(int, input().split()))
    
    cnt = 0
    for i in B_lst:
        if i in A_lst:
            a(0,A-1,i,'')

    print(f'#{tc} {cnt}')
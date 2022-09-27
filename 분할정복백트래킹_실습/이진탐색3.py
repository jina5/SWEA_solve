def search(N_lst,l,r,key,v):
    global cnt
    if l > r:
        return
    else:
        middle = (r+l) // 2
        if key == N_lst[middle]:
            cnt += 1
            return
        if key < N_lst[middle]:
            if v == None or v == 'RiGHT':
                return search(N_lst,l,middle-1,key,'LEFT')
            else:
                return
        elif key > N_lst[middle]:
            if v==None or v == 'LEFT':
                return search(N_lst,middle+1,r,key,'RIGHT')
            else:
                return
 
# 첫 줄에 테스트케이스 T
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    N_lst = list(map(int,input().split()))
    M_lst = list(map(int,input().split()))
    l = 0
    r = N-1
    cnt = 0
    for i in M_lst:
        search(N_lst,l,r,i,None)
    print(f'#{tc} {cnt}')
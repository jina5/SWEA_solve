T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split()) #컨테이너,트럭
    container=sorted(list(map(int,input().split())))
    truck=sorted(list(map(int,input().split())))
    sum=0
    c=len(container)-1
    t=len(truck)-1
    while container and truck:
        con=container[c]
        tr=truck[t]
        if con<=tr:
            sum+=con
            container.pop(c)
            truck.pop(t)
            c-=1
            t-=1
        else:
            container.pop(c)
            c-=1
    print(f'#{tc} {sum}')
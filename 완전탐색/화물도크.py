T=int(input())
for tc in range(1,T+1):
    n= int(input())
    sch=[]
    for _ in range(n):
        x,y=map(int,input().split())
        sch.append([x,y])
    sch=sorted(sch, key=lambda x:x[1])
    ok=[]
    ok.append(sch[0])
    sch.pop(0)
    for s in sch:
        if ok[-1][1]<=s[0]:
            ok.append(s)
    print(f'#{tc} {len(ok)}')
    
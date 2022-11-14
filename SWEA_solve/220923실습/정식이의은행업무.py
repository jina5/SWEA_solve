def solve(num,change):
    result=[]
    for i in range(len(num)) :
        for c in change:
            temp=num[i]
            num[i]=c
            result.append(''.join(num))
            num[i]=temp
    return result

def change(can,e):
    result=[]
    for c in can:  
        result.append(int(c,e))
    return result
        
T=int(input())
for tc in range(1,T+1):
    bi=list(input())
    tri=list(input())
    bic=change(solve(bi,['0','1']),2)
    tric=change(solve(tri,['0','1','2']),3)
    for b in bic:
        if b in tric:
            print(f'#{tc} {b}')
    
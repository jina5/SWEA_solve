def merge_sort(group):
    global cnt
    n=len(group)
    if n<=1:
        return group
    mid=n//2
    g1=merge_sort(group[:mid])
    g2=merge_sort(group[mid:])

    result=[]
    l=r=0

    if g1[-1]>g2[-1]:
        cnt+=1

    while l<len(g1) and r<len(g2):
        if g1[l]<g2[r]:
            result.append(g1[l])
            l+=1
        else:
            result.append(g2[r])
            r+=1
    if g1:
        result+=g1[l:]
    if g2:
        result+=g2[r:]
    return result  
        
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    cnt=0
    group=list(map(int,input().split()))
    result=merge_sort(group)
    print(f'#{tc} {result[n//2]} {cnt}')

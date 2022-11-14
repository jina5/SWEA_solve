def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x,y):
    parent[find_set(y)] = find_set(x)
    
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    parent = [ x for x in range(0, n+1) ]
    result=[]
    index=0
    for i in range(m):
        union(arr[2*i],arr[2*i+1])

    for i in range(1,n+1):
        p=find_set(i)
        if p not in result:
            result.append(p)
    print(f'#{tc} {len(result)}')




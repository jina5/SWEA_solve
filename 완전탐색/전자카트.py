def f(i, k):
    if i == k:
        lst.append(p[:])
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]
            
T=int(input())               
for tc in range(1,T+1):
    n=int(input())
    arr= list(list(map(int,input().split())) for _ in range(n))
    p=[i for i in range(2,n+1)] #2부터 n까지
    used=[False]*(n-1)
    lst=[]
    f(0,n-1)
    for l in lst:
        l.insert(0,1)
        l.append(1)
    min_sum=0
    for a in arr:
        min_sum+=sum(a)   
    for l in lst:
        s=0
        for i in range(len(l)-1):
            s+=arr[l[i]-1][l[i+1]-1]
        if s<min_sum:
            min_sum=s
    print(f'#{tc} {min_sum}')

    
    
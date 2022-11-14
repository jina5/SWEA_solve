def bi_search(n,arr,m):
    global flag
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==m:
            return mid
        elif arr[mid]>m:
            flag+=['l']
            r=mid-1
        else:
            flag+=['r']
            l=mid+1
           
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    m_list=list(map(int,input().split()))
    arr.sort()
    cnt=0
    for m in m_list:
        flag=[]
        result=bi_search(n,arr,m)
        if result!=None:
            if not flag or len(flag)==1:
                cnt+=1
            else:
                for i in range(1,len(flag)):
                    if flag[i]==flag[i-1]:
                        break
                else:
                    cnt+=1
    print(f'#{tc} {cnt}')

                                        
                    
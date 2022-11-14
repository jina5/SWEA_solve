def partition(left,right):
    p=arr[left]
    i,j=left,right
    while i<=j:
        while i <= j and arr[i]<=p:
            i+=1
        while i <= j and arr[j]>p:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j
    
def quick(l,r):
    if l < r:
        p_idx = partition(l, r)
        quick(l, p_idx-1)
        quick(p_idx+1, r)
    
T=int(input())
for tc in range(1,T+1):
    n = int(input())
    arr=list(map(int,input().split()))
    quick(0,n-1)
    print(f'#{tc} {arr[n//2]}')
    
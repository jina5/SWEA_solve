def inorder(node): 
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(arr1[node])
    inorder(arr2[node])

for tc in range(1, int(input()) + 1):
    E,N = map(int, input().split())
    arr = list(map(int, input().split()))
    arr1 = [0]*(E+2) 
    arr2 = [0]*(E+2) 
    for i in range(0,len(arr),2): 
        parent, child = arr[i], arr[i+1]
        if arr1[parent]:
            arr2[parent]=child 
        else: 
            arr1[parent]=child 
    cnt = 0
    inorder(N)
    print(f'#{tc} {cnt}')
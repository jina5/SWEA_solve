def inorder(node):
    global cnt
    if node <= n:
        inorder(node*2)   
        tree[node] = cnt
        cnt += 1
        inorder(node*2+1) 

for tc in range(1,int(input())+1):
    n=int(input())
    tree = [0]*(n+1)
    cnt = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[n//2]}')

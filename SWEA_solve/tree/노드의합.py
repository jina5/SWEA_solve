def tree_sum(node):
    if node<=n:
        if tree[node]:
            return tree[node]
        return tree_sum(node*2)+tree_sum(node*2+1)            
    else:
        return 0
        
T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0 for _ in range(n + 1)]
    for _ in range(m):
        i, num = map(int, input().split())
        tree[i] = num
    result=tree_sum(l)
    print(f'#{tc} {result}')
        
        
def preorder(v):
    global cnt
    v
    if v:
        cnt += 1
        preorder(tree[0][v])
        preorder(tree[1][v])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[0] * (E + 2) for _ in range(2)]
    for i in range(0, len(lst), 2):
        if tree[0][lst[i]] == 0:
            tree[0][lst[i]] = lst[i + 1]
        else:
            tree[1][lst[i]] = lst[i + 1]
    print(tree[0])
    print(tree[1])
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')
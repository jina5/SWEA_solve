def solve(v):
    #v번을 루트로 하는 트리의 노드 개수 반환
    #dfs
    stack=[v]
    cnt=0
    while stack :
        current = stack.pop()
        cnt+=1
        #현재 노드로부터 갈 수 있는 노두를 모두 stack에 push
        for i in range(2):
            if tree[i][current]:
                stack.append(tree[i][current])
    return cnt

#트리순회
def traversal(v):
    #v번을 루트로 하는 트리의 노드 개수 반환
    #리프노드는 하나 반환
    # 리프노드 아니라면 왼쪽서브트리노드개수+오른쪽서브트리노드개수+1
    #v가 유효한 노드가 아니라면 0반환
    if v == 0 :
        return 0
    else:
        return traversal(tree[0][v])+traversal(tree[1][v])+1


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
    cnt = 0
    result=solve(N)
    result=traversal(N)
    print(f'#{tc} {result}')
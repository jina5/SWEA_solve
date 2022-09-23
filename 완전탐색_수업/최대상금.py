def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return

    for i in range(L-1):
        for j in range(i+1, L):  # L개에서 2개 뽑는 조합
            # 바꾼 다음 lst를 숫자로 만들어야하니, 바꾸고 cst를 만들어야 함!!!
            lst[i], lst[j] = lst[j], lst[i]

            cst = int("".join(map(str, lst)))
            if (n, cst) not in v:   # 방문 안 한 경우
                dfs(n+1)
                v.append((n, cst))

            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for test_case in range(1, T + 1):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))

    v = []  # visited
    L = len(lst)
    ans = 0
    dfs(0)

    print(f'#{test_case} {ans}')


# -------------------------------------------------------------


def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return

    for i in range(L-1):
        for j in range(i+1, L):  # L개에서 2개 뽑는 조합
            # 바꾼 다음 lst를 숫자로 만들어야하니, 바꾸고 cst를 만들어야 함!!!
            lst[i], lst[j] = lst[j], lst[i]

            # cst = int("".join(map(str,lst)))    # list의 경우 501ms
            # if (n, cst) not in v:   # 방문 안 한 경우
            #     dfs(n+1)
            #     v.append((n,cst))

            cst = int("".join(map(str, lst)))
            if dct_v.get((n, cst), 1):  # 딕셔너리에 없는 경우(미방문) 1, 즉 true를 리턴
                dfs(n+1)
                # 반대인 경우이니 0을 저장 (그래야 get 할때 있으면 0, false를 리턴)
                dct_v[(n, cst)] = 0

            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for test_case in range(1, T + 1):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))

    v = []  # visited
    dct_v = {}  #
    L = len(lst)
    ans = 0
    dfs(0)

    print(f'#{test_case} {ans}')


# -------------------------------------------------------------/#


def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(map(str, lst))))
        return

    for i in range(L-1):
        for j in range(i+1, L):  # L개에서 2개 뽑는 조합
            # 바꾼 다음 lst를 숫자로 만들어야하니, 바꾸고 cst를 만들어야 함!!!
            lst[i], lst[j] = lst[j], lst[i]

            # cst = int("".join(map(str,lst)))    # list의 경우 501ms
            # if (n, cst) not in v:   # 방문 안 한 경우
            #     dfs(n+1)
            #     v.append((n,cst))

            cst = int("".join(map(str, lst)))        # 딕셔너리의 경우 208ms
            if dct_v.get((n, cst), 1):  # 딕셔너리에 없는 경우(미방문) 1, 즉 true를 리턴
                dfs(n+1)
                # 반대인 경우이니 0을 저장 (그래야 get 할때 있으면 0, false를 리턴)
                dct_v[(n, cst)] = 0

            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for test_case in range(1, T + 1):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))

    v = []  # visited
    dct_v = {}  #
    L = len(lst)
    ans = 0
    dfs(0)

    print(f'#{test_case} {ans}')

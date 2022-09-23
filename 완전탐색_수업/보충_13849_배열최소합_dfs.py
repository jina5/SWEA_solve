# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYM6ns9KfFMDFAU-&contestProbId=AX8j1cI6xHYDFARO&probBoxId=AYNfWrvaDIwDFAUs+&type=USER&problemBoxTitle=220921%3A+3%ED%9A%8C%EC%B0%A8&problemBoxCnt=3
def f(i, k, s):
    global minV
    if i == k:
        if minV > s:
            minV = s

    elif s > minV:          # 중간에 합이 이미 minV 보다 크면 중단
        return

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s + data[i][p[i]])
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minV = N*10
    # s = 0

    f(0, N, 0)
    print(minV)

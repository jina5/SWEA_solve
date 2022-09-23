# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYM6ns9KfFMDFAU-&contestProbId=AX7wkzAKSpEDFARO&probBoxId=AYNfWrvaDIwDFAUs+&type=USER&problemBoxTitle=220921%3A+3%ED%9A%8C%EC%B0%A8&problemBoxCnt=++3+

def dfs(n, sum, cnt):
    global ans
    if n == N:
        if sum == K and cnt == CNT:
            ans += 1
        return

    dfs(n+1, sum+lst[n], cnt+1)  # 사용하는 경우
    dfs(n+1, sum, cnt)  # 사용하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = len(lst)

    ans = 0
    dfs(0, 0, 0)

    print(f'#{tc} {ans}')

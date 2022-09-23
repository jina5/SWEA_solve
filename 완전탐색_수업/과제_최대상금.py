# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV15Khn6AN0CFAYD&solveclubId=AYJ7fdTqLYoDFASv&problemBoxTitle=220921_%EA%B3%BC%EC%A0%9C%EB%B0%8F%EC%8B%A4%EC%8A%B5&problemBoxCnt=1&probBoxId=AYNeRpSaCRMDFASV+

def f(n, cnt):
    global maxV
    if n == cnt:
        tmp = int(''.join(num))
        if maxV < tmp:
            maxV = tmp
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                tmp = int(''.join(num))
                if tmp not in u[n]:
                    u[n].append(tmp)
                    f(n+1, cnt)
                num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, 1+T):
    num, cnt = input().split()
    num = list(num)
    cnt = int(cnt)
    maxV = 0
    u = [[] for _ in range(10)]
    f(0, cnt)
    print(f'#{tc} {maxV}')

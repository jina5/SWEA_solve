
def f(i, k):
    global ans
    if i == k:
        run = 0
        tri = 0
        # print(card)
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0]+1 == card[1] and card[1]+1 == card[2]:
            run += 1
        if card[3] == card[4] and card[4] == card[5]:
            tri += 1
        if card[3]+1 == card[4] and card[4]+1 == card[5]:
            run += 1

        if tri+run == 2:
            return 1
        else:
            return 0

    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            if f(i+1, k):                      # 답 찾았으면
                return 1                       # return 1 리턴하고 끝내자
            card[i], card[j] = card[j], card[i]
        return 0                               # for문 다 돌았는데도 안나왔으면 0리턴


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    ans = f(0, 6)

    if ans:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')

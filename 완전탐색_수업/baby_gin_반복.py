from tkinter import E


T = int(input())
for tc in range(1, T+1):
    card = int(input())
    c = [0] * 12  # run 검사 위해 여유롭게 뒤에 두 칸 더 넣음, 첫 칸[0]엔 뭐 안들어감 어차피

    # card 카운트해서 c에 표시
    i = 0
    while i < 6:
        c[card % 10] += 1
        card //= 10
        i += 1

    tri = 0
    run = 0
    i = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1

    if tri + run == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')

import sys
sys.stdin = open('input.txt', 'r')

# 거꾸로 뒤집으면 1이 있기 때문에 인식하기 좋음
keydict = {
    '1011000':'0',
    '1001100':'1',
    '1100100':'2',
    '1011110':'3',
    '1100010':'4',
    '1000110':'5',
    '1111010':'6',
    '1101110':'7',
    '1110110':'8',
    '1101000':'9'
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = ''
    arr = [input()[::-1] for _ in range(N)]
    for a in arr:
        lst = a
        if '1' in lst:
            for m in range(M):
                if lst[m] == '1':
                    for i in range(m, M, 7):
                        result += keydict[lst[i:i+7]]
                        if len(result) == 8:
                            break
                if len(result) == 8:
                    break
        if len(result) == 8:
            break

    result2 = result[::-1]
    is_key = 0
    odd_sum = 0
    even_sum = 0
    # 홀수자리(인덱스가 짝수), 짝수자리(인덱스가 홀수)
    for char in range(8):
        if char%2 == 0:
            odd_sum += int(result2[char])
        else:
            even_sum += int(result2[char])
    is_key = odd_sum*3 + even_sum

    answer = 0
    if is_key%10==0:
        for j in result2:
            answer += int(j)
    else:
        answer = 0

    print(f'#{tc} {answer}')
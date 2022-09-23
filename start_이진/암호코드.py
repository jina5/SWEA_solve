hex_dic = {
'0' : [0,0,0,0],
'1' : [0,0,0,1],
'2' : [0,0,1,0],
'3' : [0,0,1,1],
'4' : [0,1,0,0],
'5' : [0,1,0,1],
'6' : [0,1,1,0],
'7' : [0,1,1,1],
'8' : [1,0,0,0],
'9' : [1,0,0,1],
'A' : [1,0,1,0],
'B' : [1,0,1,1],
'C' : [1,1,0,0],
'D' : [1,1,0,1],
'E' : [1,1,1,0],
'F' : [1,1,1,1]
}
code_dic = {
(3,2,1,1) : 0,
(2,2,2,1) : 1,
(2,1,2,2) : 2,
(1,4,1,1) : 3,
(1,1,3,2) : 4,
(1,2,3,1) : 5,
(1,1,1,4) : 6,
(1,3,1,2) : 7,
(1,2,1,3) : 8,
(3,1,1,2) : 9
}

#2진 암호코드를 읽기
def solve():
    result = 0
    for i in range(N):
        #16진수를 4개 비트로 변경했으니 전체길이가 4배 늘어남
        j = M*4-1
        while j >= 55:
            # 뒤에서 부터 볼건데 만약에 1이면, 코드 읽기 시작
            if bin_data[i][j] == 1 and bin_data[i-1][j] == 0:
                code = []
                for _ in range(8):
                    n1 = n2 = n3 = n4 = 0
                    while bin_data[i][j] == 1:
                        n4 += 1
                        j -=1

                    while bin_data[i][j] == 0:
                        n3 += 1
                        j -= 1

                    while bin_data[i][j] == 1:
                        n2 += 1
                        j -= 1
                    # n2,n3,n4 중에서 가장 작은 수가
                    # 현재 늘어난 비율을 의미
                    rate = min(n2,n3,n4)
                    n2 //= rate
                    n3 //= rate
                    n4 //= rate
                    n1 = 7 - n2 - n3 - n4
                    j -= n1*rate
                    code.append(code_dic[(n1,n2,n3,n4)])
                # 숫자 8자리 확인 끝!
                # 정상적인 암호인지 확인하기
                code.reverse()  # 뒤에서 부터 작성했으니 뒤집기
                odd_num = code[0] + code[2] + code[4] + code[6]
                even_num = code[1] + code[3] + code[5] + code[7]
                if (odd_num*3 + even_num) % 10 == 0:
                    result += odd_num + even_num
            else:   #암호코드가 끝나는 지점이 아니면, 다음칸 확인
                j -= 1
    return result

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in  range(N)]
    # 16진수를 2진수 데이터로 변경
    bin_data = []
    for i in range(N):
        tmp = []
        for j in range(M):
            tmp += hex_dic[data[i][j]]
        bin_data.append(tmp)
    # 암호코드 찾아서 읽기
    result = solve()
    # 결과 출력
    print(f'#{tc} {result}')


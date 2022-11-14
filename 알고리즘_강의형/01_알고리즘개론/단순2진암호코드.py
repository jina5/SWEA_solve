T=int(input())
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

for tc in range(1,T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    result=0
    for i in range(N):
        for j in range(M-1, 54,-1):
            if data[i][j] == 1: 
                code=[]
                for _ in range(8):  
                    n1 = n2 = n3 = n4 = 0
                    while data[i][j] == 1:
                        n4 += 1
                        j -= 1
                    while data[i][j] == 0:
                        n3 += 1
                        j -= 1
                    while data[i][j] == 1:
                        n2 += 1
                        j -= 1
                    n1 = 7 - n2 - n3 - n4
                    j -= n1
                    code.append(code_dic[(n1,n2,n3,n4)])
                odd_nums = code[1] + code[3] + code[5] + code[7]
                even_nums = code[0] + code[2] + code[4] + code[6]
                if (odd_nums*3+ even_nums) % 10 == 0:
                    result = odd_nums + even_nums
                    break
                break

    print(f'#{tc} {result}')                    
                    
    
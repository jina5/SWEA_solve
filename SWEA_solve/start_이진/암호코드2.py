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
 
def hex_bi(h):
    n=int(h,16)
    re=''
    for i in range(3,-1,-1):
        re += '1' if n & (1<<i) else '0'
    return re
 
T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    code_list=[]
    for _ in range(N):
        data = input().strip()
        for i in range(M):
            if data[i] !='0':
                output=''
                for d in data:
                    output += hex_bi(d)
                code_list.append(output)
                break
    code_list=set(code_list)
    result=[]
    result_list=[]
    for code in code_list:
        n = len(code) -1
        while n >= 55 :
            if code[n] != '1':
                n-=1
            else:
                c=[]
                for _ in range(8):
                    n1=n2=n3=n4=0
                    while code[n] =='1':
                        n4+=1
                        n-=1
                    while code[n] =='0':
                        n3+=1
                        n-=1
                    while code[n] =='1':
                        n2+=1
                        n-=1
                    m=min(n2,n3,n4)
                    n1= 7*m - n2-n3-n4
                    n-=n1
                    try:
                        c.append(code_dic[(n1//m,n2//m,n3//m,n4//m)])
                    except:
                        break
                try:
                    odd_nums = c[1] + c[3] + c[5] + c[7]
                    even_nums = c[0] + c[2] + c[4] + c[6]
                    if (odd_nums * 3 + even_nums) % 10 == 0:
                            if c not in result:
                                result.append(c)
                                result_list.append(odd_nums + even_nums)
                except:
                    pass
    print(f'#{tc} {sum(result_list)}')
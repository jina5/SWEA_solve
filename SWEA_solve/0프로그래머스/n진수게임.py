def to_n(number, base):
    T="0123456789ABCDEF"
    i,j=divmod(number,base)
    if i==0:
        return T[j]
    else:
        return to_n(i,base)+T[j]
def solution(n, t, m, p):
    answer = ''
    num=0
    while len(answer)<t*m:
        answer+=to_n(num,n)
        num+=1
    answer=answer[:t*m]
    answer=answer[p-1::m]
    return answer

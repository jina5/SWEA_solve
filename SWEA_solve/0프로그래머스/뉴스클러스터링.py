
def slice(str):
    group=[]
    for i in range(len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            group.append(str[i:i+2])
    return group

def solution(str1, str2):
    str1=slice(str1)
    str2=slice(str2)
    cnt=0
    if not str1 and not str2:
        return 65536
    for s in str1:
        if s in str2:
            cnt+=1
            str2.remove(s)
    answer = int((cnt/(len(str1)+len(str2)))*65536)
    return answer


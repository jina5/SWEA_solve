T = int(input())

num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def bi(n):
    ans=''
    for i in range(3,-1,-1):
        ans+='1' if int(n) & (1<<i) else '0'
    return ans

for tc in range(1,T+1):
    n,hex=input().split()
    result=''
    for h in hex:
        if h in num:
            h=num[h]
        result=result+bi(h)
    print(f'#{tc} {result}')
        
        
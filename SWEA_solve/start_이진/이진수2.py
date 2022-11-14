def bi(f):
    ans=''
    cnt=0
    while f*2!=0:
        ans=ans+str(int((f*2)//1))
        f=(f*2)%1
        cnt+=1
        if cnt>12:
            return 'overflow'
    return ans

T=int(input())
for tc in range(1,T+1):
    f=float(input())
    print(f'#{tc} {bi(f)}')
    
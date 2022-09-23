T=int(input())
for tc in range(1,T+1):
    n=int(input())
    result=round(n**(1/3))
    if n!=result**3:
        result=-1
    print(f'#{tc} {result}')
            